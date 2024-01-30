import tkinter as tk
from tkinter import filedialog

def encrypt_decrypt_image(path, key, operation):
    try:
        with open(path, 'rb') as fin:
            image = bytearray(fin.read())

        for index, values in enumerate(image):
            image[index] = values ^ key

        with open(path, 'wb') as fout:
            fout.write(image)

        result_label.config(text=f'{operation} Done...')

    except FileNotFoundError:
        result_label.config(text='Error: File not found.')
    except ValueError:
        result_label.config(text='Error: Invalid key. Please enter a valid integer key.')
    except Exception as e:
        result_label.config(text=f'Error caught: {type(e).__name__} - {e}')

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def process_encryption():
    path = file_entry.get()
    key = int(key_entry.get())
    encrypt_decrypt_image(path, key, 'Encryption')

def process_decryption():
    path = file_entry.get()
    key = int(key_entry.get())
    encrypt_decrypt_image(path, key, 'Decryption')

# GUI setup
root = tk.Tk()
root.title("Image Encryption and Decryption")

# File Path Entry
file_label = tk.Label(root, text="File Path:")
file_label.pack()

file_entry = tk.Entry(root, width=50)
file_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Encryption Key Entry
key_label = tk.Label(root, text="Encryption/Decryption Key:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

# Buttons for Encryption and Decryption
encrypt_button = tk.Button(root, text="Encrypt", command=process_encryption)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=process_decryption)
decrypt_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
