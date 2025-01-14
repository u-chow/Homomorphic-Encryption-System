# B Company - Key Generation
from phe import paillier

# Generate public and private keys
public_key, private_key = paillier.generate_paillier_keypair()

# Save the public key
with open("public_key.txt", "w") as f:
    f.write(str(public_key.n))

# Save the private key
with open("private_key.txt", "w") as f:
    f.write(f"{private_key.p}\n{private_key.q}")

print("Public and private keys have been generated and saved.")