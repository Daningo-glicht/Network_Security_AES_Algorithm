from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16) 
data = b"Hello, this is a secret message"

# Encrypt
cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(data, AES.block_size))
iv = cipher.iv  # Initialization vector

print("Original:", data.decode('utf-8'))       
print("Encrypted (hex):", ciphertext.hex())

# Decrypt
decipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Decrypted:", plaintext.decode('utf-8'))  


