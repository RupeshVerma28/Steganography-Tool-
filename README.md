# 🕵️‍♂️ Image Steganography Tool
A simple and secure desktop GUI application for hiding secret messages inside image files using Python and CustomTkinter.

## 🚀 Features
- Hide (encode) secret text messages inside PNG, JPG, and JPEG images
- Retrieve (decode) hidden messages from stego images
- Modern dark-themed GUI using `CustomTkinter`
- Easy-to-use interface with message box and file dialogs

## 📦 Tech Stack
- Python
- CustomTkinter
- Pillow (PIL)
 📥 Installation
1. Clone this repository:
```bash
https://github.com/RupeshVerma28/Steganography-Tool-.git
```

2. Install required packages:
```bash
pip install customtkinter pillow
```

3. Run the app:
```bash
python steganography_gui.py
```

## 💡 How It Works
- Converts your message into binary
- Replaces the least significant bits (LSBs) of the image pixels with the binary data
- Decoding reverses the process and stops at a unique `###` marker

## 🖼️ Screenshot
![image](https://github.com/user-attachments/assets/f7497b19-8bcb-4001-981d-1e4a9d158496)


## 📁 File Structure

image-steganography-tool/
├── steganography_gui.py
├── README.md
└── requirements.txt (optional)


## ⚠️ Disclaimer
This tool is for educational purposes. For stronger data security, consider encrypting the message before encoding.

## 🛠️ Future Enhancements
- Password protection (AES encryption)
- Image preview feature
- Export as Windows .exe

## 📃 License
MIT License

## 🙋‍♂️ Author
**Rupseh Verma**  
BCA | Cyber Security Enthusiast | Ethical Hacker 

