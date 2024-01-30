def encrypt_decrypt_image(path, key, operation):
    try:
        # open file for reading purpose
        with open(path, 'rb') as fin:
            # storing image data in variable "image"
            image = bytearray(fin.read())

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # open file for writing purpose
        with open(path, 'wb') as fout:
            # writing encryption/decryption data in image
            fout.write(image)

        print(f'{operation} Done...')

    except FileNotFoundError:
        print('Error: File not found.')
    except ValueError:
        print('Error: Invalid key. Please enter a valid integer key.')
    except Exception as e:
        print(f'Error caught: {type(e).__name__} - {e}')

# Encryption
path_encrypt = input(r'Enter path of Image for Encryption: ')
key_encrypt = int(input('Enter Key for Encryption: '))
encrypt_decrypt_image(path_encrypt, key_encrypt, 'Encryption')

# Decryption
path_decrypt = input(r'Enter path of Image for Decryption: ')
key_decrypt = int(input('Enter Key for Decryption: '))
encrypt_decrypt_image(path_decrypt, key_decrypt, 'Decryption')
