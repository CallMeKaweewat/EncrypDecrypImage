import os
import tkinter as tk
from tkinter import filedialog
import tempfile
import shutil
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

def encrypt_decrypt_image(file_path, key, operation):
    try:
        with open(file_path, 'rb') as fin:
            image = bytearray(fin.read())

        for index, values in enumerate(image):
            image[index] = values ^ key

        # Use a temporary file to avoid overwriting the original
        temp_file_path = tempfile.mktemp()
        with open(temp_file_path, 'wb') as fout:
            fout.write(image)

        # Move the temporary file to the original file
        shutil.move(temp_file_path, file_path)

        result_label.config(text=f'{operation} Done for {file_path}.')

    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        result_label.config(text=f'Error: File not found - {file_path}')
    except ValueError:
        logging.error('Invalid key value')
        result_label.config(text='Error: Invalid key. Please enter a valid integer key.')
    except Exception as e:
        logging.exception(f'Error caught: {type(e).__name__} - {e}')
        result_label.config(text=f'Error caught: {type(e).__name__} - {e}')

def browse_file_or_directory():
    path = filedialog.askopenfilename() if operation_var.get() == "Single Image" else filedialog.askdirectory()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, path)
    operation_var.set("Single Image" if os.path.isfile(path) else "All Images")

def process_encryption_decryption():
    selected_operation = operation_var.get()
    key = int(key_entry.get())
    file_path = file_entry.get()

    try:
        if selected_operation == "Single Image" and os.path.isfile(file_path):
            encrypt_decrypt_image(file_path, key, 'Encryption/Decryption')
        elif selected_operation == "All Images" and os.path.isdir(file_path):
            for filename in os.listdir(file_path):
                image_path = os.path.join(file_path, filename)
                if os.path.isfile(image_path):
                    encrypt_decrypt_image(image_path, key, 'Encryption/Decryption')
        else:
            logging.error('Invalid file or directory path')
            result_label.config(text='Error: Invalid file or directory path.')
    except Exception as e:
        logging.exception(f'Unexpected error: {type(e).__name__} - {e}')

# GUI setup
root = tk.Tk()
root.title("Image Encryption and Decryption")

# Operation Selection
operation_var = tk.StringVar()
operation_var.set("Single Image")

operation_label = tk.Label(root, text="Select Operation:")
operation_label.pack()

single_image_radio = tk.Radiobutton(root, text="Single Image", variable=operation_var, value="Single Image")
single_image_radio.pack()

all_images_radio = tk.Radiobutton(root, text="All Images", variable=operation_var, value="All Images")
all_images_radio.pack()

# File/Directory Path Entry
file_label = tk.Label(root, text="File/Directory Path:")
file_label.pack()

file_entry = tk.Entry(root, width=50)
file_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file_or_directory)
browse_button.pack()

# Encryption Key Entry
key_label = tk.Label(root, text="Encryption/Decryption Key:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

# Button for Encryption/Decryption
process_button = tk.Button(root, text="Encrypt/Decrypt", command=process_encryption_decryption)
process_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
