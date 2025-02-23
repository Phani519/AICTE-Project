import cv2
import os
import tkinter as tk
from tkinter import messagebox

# Function to encrypt the message into the image
def encrypt_message():
    msg = entry_message.get()
    password = entry_password.get()
    
    if not msg or not password:
        messagebox.showerror("Error", "Please enter both a message and a password.")
        return
    
    img = cv2.imread("mypic.jpg")
    if img is None:
        messagebox.showerror("Error", "Image file 'Astro.jpg' not found.")
        return
    
    if len(msg) > img.shape[0] * img.shape[1] * 3:
        messagebox.showerror("Error", "Message is too long to fit in the image.")
        return
    
    encrypted_msg = []
    key = sum(ord(char) for char in password) % 256
    for char in msg:
        encrypted_msg.append(ord(char) ^ key)

    index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3): 
                if index < len(encrypted_msg):
                    img[i, j, k] = encrypted_msg[index]
                    index += 1
                else:
                    break
            if index >= len(encrypted_msg):
                break
        if index >= len(encrypted_msg):
            break
    encrypted_img_path = "encryptedImage.png"
    cv2.imwrite("encryptedImage.png", img)
    messagebox.showinfo("Success", "Message encrypted and saved as 'encryptedImage.png'.")
    os.system(f"start {encrypted_img_path}")

# Function to decrypt the message from the image
def decrypt_message():
    password = entry_password.get()
    pas = entry_decrypt_password.get()
    
    if password != pas:
        messagebox.showerror("Error", "Incorrect password for decryption.")
        return
    
    img = cv2.imread("encryptedImage.png")
    if img is None:
        messagebox.showerror("Error", "Encrypted image file 'encryptedImage.png' not found.")
        return
    
    key = sum(ord(char) for char in password) % 256  
    decrypted_msg = []
    index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3): 
                decrypted_msg.append(chr(img[i, j, k] ^ key))
                index += 1
                if index >= len(entry_message.get()):
                    break
            if index >= len(entry_message.get()):
                break
        if index >= len(entry_message.get()):
            break
    
    decrypted_msg = ''.join(decrypted_msg).rstrip('\x00')
    
    messagebox.showinfo("Decrypted Message", f"Decrypted message: {decrypted_msg}")

root = tk.Tk()
root.title("Steganography App")
root.geometry("400x300")

label_message = tk.Label(root, text="Enter Secret Message:")
label_message.pack(pady=5)
entry_message = tk.Entry(root, width=40)
entry_message.pack(pady=5)

label_password = tk.Label(root, text="Enter Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, width=40, show="*")
entry_password.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt Message", command=encrypt_message)
encrypt_button.pack(pady=10)

label_decrypt_password = tk.Label(root, text="Enter Password for Decryption:")
label_decrypt_password.pack(pady=5)
entry_decrypt_password = tk.Entry(root, width=40, show="*")
entry_decrypt_password.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt Message", command=decrypt_message)
decrypt_button.pack(pady=10)

root.mainloop()