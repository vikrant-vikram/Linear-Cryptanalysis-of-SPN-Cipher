
import spn as cipher
import itertools as it
import collections
from math import fabs
from lat import lat
import basic_methods as bm
from express import express
from spn_supplymentary import sbox_inv, sbox_inv1

# ANSI color codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"

# Display the probability bias table for analysis
def linear_cryptanalysis(plaintext, key):
    """
    Performs linear cryptanalysis on the given plaintext and key.

    Parameters:
    plaintext (str): The input plaintext (binary string).
    key (str): The encryption key (binary string).

    Returns:
    None: Prints the analysis results, including the estimated subkey.
    """
    # Default values for plaintext and key if none provided
    lat()

    if not plaintext:
        plaintext = list('0010011010110111')  # Example default plaintext
    if not key:
        key = bm.random_36bit_string()  # Generate a random 36-bit key

    # Generate round keys using the cipher's key scheduling function
    round_keys = cipher.key_generator(key)

    # Analyze the fifth-round key
    fifth_round_key = round_keys[-1]  # Last 16 bits of the key
    key_segment_5_to_8 = fifth_round_key[4:8]  # Bits 5 to 8 of the fifth-round key
    key_segment_13_to_16 = fifth_round_key[12:16]  # Bits 13 to 16 of the fifth-round key

    # Print key information for debugging
    print(f'\n{CYAN}Encryption key: {key}{RESET}')
    print(f'{BLUE}Fifth-round key: {fifth_round_key}{RESET}')
    print(f'{GREEN}Segment K5[5:8]: {key_segment_5_to_8}{RESET}')
    print(f'{YELLOW}Segment K5[13:16]: {key_segment_13_to_16}{RESET}')

    # Initialize an array to count biases for each potential subkey
    subkey_bias_counts = [0] * 256  # 256 possible subkey values (8 bits)

    # Test on 10,000 random plaintexts
    for plaintext_int in range(10000):
        # Convert plaintext integer to a 16-bit binary string
        binary_plaintext = bm.int_to_16bit_binary(plaintext_int)

        # Encrypt the plaintext and convert the ciphertext to an integer
        ciphertext = int(cipher.encrypt(binary_plaintext, key), 2)

        # Extract bits 5 to 8 and 13 to 16 from the ciphertext
        ciphertext_segment_5_to_8 = (ciphertext >> 8) & 0b1111
        ciphertext_segment_13_to_16 = ciphertext & 0b1111

        # Test all possible subkey values
        for subkey_candidate in range(256):
            subkey_candidate_5_to_8 = (subkey_candidate >> 4) & 0b1111
            subkey_candidate_13_to_16 = subkey_candidate & 0b1111

            # Perform XOR between ciphertext and subkey candidates
            xor_5_to_8 = ciphertext_segment_5_to_8 ^ subkey_candidate_5_to_8
            xor_13_to_16 = ciphertext_segment_13_to_16 ^ subkey_candidate_13_to_16

            # Apply the inverse S-Box to the XOR results
            inv_sbox_output_5_to_8 = sbox_inv1[xor_5_to_8]
            inv_sbox_output_13_to_16 = sbox_inv1[xor_13_to_16]

            # Evaluate the linear approximation for the given plaintext
            linear_approximation = express(inv_sbox_output_5_to_8, inv_sbox_output_13_to_16, plaintext_int)
            if linear_approximation == 0:
                subkey_bias_counts[subkey_candidate] += 1

    # Calculate biases for each subkey candidate
    biases = [abs(count - 5000.0) / 10000.0 for count in subkey_bias_counts]
    highest_bias, best_subkey = max(biases), biases.index(max(biases))

    # Convert the best subkey candidate to a 16-bit binary string
    estimated_subkey = bm.hex_to_binary_16bit(hex(best_subkey))

    # Print the results
    get_top_ten = lambda lst: sorted(enumerate(lst), key=lambda x: x[1], reverse=True)[:10]
    top_ten = get_top_ten(biases)
    print("Top 10 Candidate keys:")
    for index, value in top_ten:
        print(f"key: {bm.hex_to_binary_16bit(hex(index))}, bias: {value}")

    print(f'{RED}Highest bias: {highest_bias}{RESET}')
    print(f'{CYAN}Estimated subkey value: {estimated_subkey}{RESET}')
    if (key_segment_5_to_8 + key_segment_13_to_16) == estimated_subkey:
        print(f'{GREEN}The estimated subkey is correct!{RESET}')
    else:
        print(f'{RED}The estimated subkey is incorrect!{RESET}')
