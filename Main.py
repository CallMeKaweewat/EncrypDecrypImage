import os
import tkinter as tk
from tkinter import filedialog
import tempfile
import shutil

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as fin:
            content = bytearray(fin.read())

        for index, values in enumerate(content):
            content[index] = values ^ key

        # Use a temporary file to avoid overwriting the original
        temp_file_path = tempfile.mktemp()
        with open(temp_file_path, 'wb') as fout:
            fout.write(content)

        # Move the temporary file to the original file
        shutil.move(temp_file_path, file_path)

        result_label.config(text=f'Encryption Done for {file_path}.')

    except FileNotFoundError:
        result_label.config(text=f'Error: File not found - {file_path}')
    except ValueError:
        result_label.config(text='Error: Invalid key. Please enter a valid integer key.')
    except Exception as e:
        result_label.config(text=f'Error caught: {type(e).__name__} - {e}')

def decrypt_file(file_path, key):
    # Implement decryption logic here
    # Similar to the encrypt_file function but with the inverse operation

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)
    operation_var.set("Single File")

def browse_directory():
    directory_path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory_path)
    operation_var.set("All Files")

def clear_result_label():
    result_label.config(text="")

def process_encryption_decryption():
    selected_operation = operation_var.get()
    key = int(key_entry.get())
    file_path = file_entry.get()

    if selected_operation == "Encrypt":
        encrypt_file(file_path, key)
    elif selected_operation == "Decrypt":
        decrypt_file(file_path, key)

# GUI setup
root = tk.Tk()
root.title("File Encryption and Decryption")

# Operation Selection
operation_var = tk.StringVar()
operation_var.set("Encrypt")

operation_label = tk.Label(root, text="Select Operation:")
operation_label.pack()

encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=operation_var, value="Encrypt")
encrypt_radio.pack()

decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=operation_var, value="Decrypt")
decrypt_radio.pack()

# File/Directory Path Entry
file_label = tk.Label(root, text="File/Directory Path:")
file_label.pack()

file_entry = tk.Entry(root, width=50)
file_entry.pack()

browse_button = tk.Button(root, text="Browse", command=lambda: browse_file())
browse_button.pack()

# Directory Entry
directory_label = tk.Label(root, text="Directory Path (for All Files):")
directory_label.pack()

directory_entry = tk.Entry(root, width=50)
directory_entry.pack()

# Encryption Key Entry
key_label = tk.Label(root, text="Encryption/Decryption Key:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

# Button for Encryption/Decryption
process_button = tk.Button(root, text="Process", command=process_encryption_decryption)
process_button.pack()

# Clear Data Button
clear_button = tk.Button(root, text="Clear Data", command=clear_result_label)
clear_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
