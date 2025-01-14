# B Company - Data Decryption
from phe import paillier

# Load B Company's public key
with open("public_key.txt", "r") as f:
    n = int(f.read())
public_key = paillier.PaillierPublicKey(n)

# Load B Company's private key
with open("private_key.txt", "r") as f:
    p, q = map(int, f.readlines())
private_key = paillier.PaillierPrivateKey(public_key, p, q)

# Load the encrypted data
with open("encrypted_data.txt", "r") as f:
    ciphertext = int(f.readline().strip())
    exponent = int(f.readline().strip())

# Reconstruct the encrypted object
encrypted_data = paillier.EncryptedNumber(public_key, ciphertext, exponent)

# Decrypt the data
decrypted_int = private_key.decrypt(encrypted_data)

# Attempt to decode the decrypted data
try:
    # Convert integer back to bytes and decode
    decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
    decrypted_data = decrypted_bytes.decode('utf-8')
    print(f"Decrypted data: {decrypted_data}")
except UnicodeDecodeError:
    # If not text, print as number
    print(f"Decrypted data (numeric): {decrypted_int}")