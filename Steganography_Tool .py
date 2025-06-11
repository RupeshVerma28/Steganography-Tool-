import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Image Steganography Tool")
app.geometry("500x600")

selected_image_path = ""

# Encode Message into Image
def encode_message(img_path, message):
    img = Image.open(img_path).convert('RGB')
    binary_msg = ''.join(format(ord(i), '08b') for i in message + '###')
    pixels = img.load()

    data_index = 0
    for y in range(img.height):
        for x in range(img.width):
            if data_index < len(binary_msg):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_msg[data_index])
                data_index += 1
                if data_index < len(binary_msg):
                    g = (g & ~1) | int(binary_msg[data_index])
                    data_index += 1
                if data_index < len(binary_msg):
                    b = (b & ~1) | int(binary_msg[data_index])
                    data_index += 1
                pixels[x, y] = (r, g, b)
    return img

# Decode Message from Image
def decode_message(img_path):
    img = Image.open(img_path).convert('RGB')
    pixels = img.load()
    binary_data = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ""
    for byte in all_bytes:
        decoded += chr(int(byte, 2))
        if decoded.endswith("###"):
            break
    return decoded[:-3]

# UI Functions
def browse_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if selected_image_path:
        img_label.configure(text=f"Selected: {os.path.basename(selected_image_path)}")

def encode_action():
    msg = message_entry.get("0.0", ctk.END).strip()
    if not selected_image_path or not msg:
        messagebox.showerror("Error", "Select an image and enter a message.")
        return
    encoded_img = encode_message(selected_image_path, msg)
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        encoded_img.save(save_path)
        messagebox.showinfo("Success", "Message encoded and image saved.")

def decode_action():
    global selected_image_path
    if not selected_image_path:
        messagebox.showerror("Error", "Select an encoded image.")
        return
    msg = decode_message(selected_image_path)
    messagebox.showinfo("Decoded Message", msg)

# UI Layout
ctk.CTkLabel(app, text="Image Steganography Tool", font=("Arial", 20, "bold")).pack(pady=20)

ctk.CTkButton(app, text="Select Image", command=browse_image).pack(pady=10)
img_label = ctk.CTkLabel(app, text="No image selected", wraplength=400)
img_label.pack()

ctk.CTkLabel(app, text="Enter Secret Message:").pack(pady=10)
message_entry = ctk.CTkTextbox(app, height=120, width=400, border_width=2, border_color="gray")
message_entry.pack(pady=5)

ctk.CTkButton(app, text="Encode Message", command=encode_action).pack(pady=10)
ctk.CTkButton(app, text="Decode Message", command=decode_action).pack(pady=10)

app.mainloop()

