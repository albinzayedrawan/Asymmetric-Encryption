# Given values
n = 3233
phi_n = 3120
e = 7
d = 1783

# Message to encrypt
message = "CRYPTOGRAPHY"

# Function to convert a character to ASCII value
def encrypt_message(message, e, n):
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, d, n):
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Encrypting the message
encrypted_message = encrypt_message(message, e, n)

# Decrypting the message
decrypted_message = decrypt_message(encrypted_message, d, n)

encrypted_message, decrypted_message