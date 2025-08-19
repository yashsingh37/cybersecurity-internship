from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
print("[+] Key generated successfully!")

# Save the key to a file
with open("secret.key", "wb") as key_file:
    key_file.write(key)
print("[+] Key saved to secret.key")

# Load the key
with open("secret.key", "rb") as key_file:
    loaded_key = key_file.read()
print("[+] Key loaded successfully!")

# Create Fernet object
fernet = Fernet(loaded_key)

# Example text to encrypt
message = "This is a secret message."
print("[+] Original message:", message)

# Encrypt the message
encrypted = fernet.encrypt(message.encode())
print("[+] Encrypted message:", encrypted)

# Decrypt the message
decrypted = fernet.decrypt(encrypted).decode()
print("[+] Decrypted message:", decrypted)
