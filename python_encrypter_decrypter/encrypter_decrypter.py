# pip install cryptography - Inorder to resolve all the dependencies
from cryptography.fernet import Fernet

# Encode a string-message
message = "This is my secret message, sshhh!".encode()

# Generate a key
key = Fernet.generate_key()
f = Fernet(key)

# Encrypt the message
# You can use the below to send someone a secret message
encrypted = f.encrypt(message)

# Just to see how the encrypted message looks like:
print(encrypted)

# Decrypt the message
decrypted = f.decrypt(encrypted)

# Check if it has successfully decrypted
print(decrypted)
