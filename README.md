Steganography App
A simple steganography application using Python and OpenCV to hide and retrieve secret messages in an image.

Features
Encrypt Message: Hide a secret message inside an image using a password.
Decrypt Message: Retrieve the hidden message using the correct password.
Graphical Interface: Built with Tkinter for easy use.
Requirements
Ensure you have Python installed and install the required libraries:

pip install opencv-python tkinter

Run the Script:

python stego.py

Encrypt a Message:
Enter a secret message and a password.
Click "Encrypt Message" to embed it into mypic.jpg.
The encrypted image is saved as encryptedImage.png.

Decrypt a Message:
Enter the correct password used for encryption.
Click "Decrypt Message" to retrieve the hidden text.

Notes
Ensure mypic.jpg exists in the same directory as the script.
If the password is incorrect, the decryption will fail.

License
This project is open-source and available for modification. Feel free to use and improve it! 😊
