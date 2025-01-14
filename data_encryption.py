# A Company - Data Encryption
from phe import paillier

# Load B Company's public key
with open("public_key.txt", "r") as f:
    n = int(f.read())
public_key = paillier.PaillierPublicKey(n)

# User input for sensitive data
sensitive_data = input("Enter sensitive data (supports text, numbers, or mixed): ")

# Determine data type and convert to integer
if sensitive_data.isdigit():
    # Numeric input
    sensitive_int = int(sensitive_data)
else:
    # Text or mixed input
    sensitive_bytes = sensitive_data.encode('utf-8')
    sensitive_int = int.from_bytes(sensitive_bytes, byteorder='big')

# Encrypt the data
encrypted_data = public_key.encrypt(sensitive_int)

# Save the ciphertext and exponent for transmission
with open("encrypted_data.txt", "w") as f:
    f.write(f"{encrypted_data.ciphertext()}\n{encrypted_data.exponent}")

print("Data has been encrypted and saved to encrypted_data.txt.")