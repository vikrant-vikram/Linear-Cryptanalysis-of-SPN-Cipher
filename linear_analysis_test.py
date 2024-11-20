import linear_analysis as la
import basic_methods as bm
# Default values for plaintext and key
DEFAULT_PLAINTEXT = '0010011010110111'
DEFAULT_KEY = '101110001010101101110101011001000101101101'

print("Leave emepty to use default values")
user_plaintext = input("Enter the plaintext (16-bit binary string): ").strip()
if not user_plaintext:
    user_plaintext = DEFAULT_PLAINTEXT  # Use default plaintext if none is provided

user_key = input("Enter the key (36-bit binary string): ").strip()
if not user_key:
    user_key = bm.random_36bit_string()  # Generate a random key if none is provided

# Encrypt the plaintext using the SPN cipher
encrypted_text = la.linear_cryptanalysis(user_plaintext, user_key)

# Display the result
# print("Ciphertext:", encrypted_text)
