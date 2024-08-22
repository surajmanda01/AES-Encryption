from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

print("Welcome to AES Encryption")

# Message to encrypt
message = input("Please enter the message you want to encrypt: ").encode()

# Generating a key 
key = get_random_bytes(16)

# Generating an IV 
iv = get_random_bytes(AES.block_size)

# Initialize the cipher for encryption
cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)

# Padding the message
padded_message = pad(message, AES.block_size)

# Encrypt the message 
cipher_text = cipher_encrypt.encrypt(padded_message)

# print the cipher text message
print("Cipher text: ", cipher_text)
print("IV: ", iv)

# Initialize the cipher for Decryption
cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)

# Decrypting the message
decrypted_pad_message = cipher_decrypt.decrypt(cipher_text)

# Remove the Padding
original = unpad(decrypted_pad_message,AES.block_size)

# Print the Decrypted Message
print("Decrypted Message: ", original.decode())
