
def express(u_5_8, u_13_16, plaintext):
    """
    Computes a linear approximation based on the input parameters.

    Parameters:
        u_5_8 (int): Intermediate value from bits 5 to 8 after S-box processing.
        u_13_16 (int): Intermediate value from bits 13 to 16 after S-box processing.
        plaintext (int): The original plaintext represented as an integer.

    Returns:
        int: Result of the XOR-based linear approximation.
    """
    # Extract specific bits from u_5_8 and u_13_16
    bit_3_of_u_5_8 = (u_5_8 >> 2) & 0b1
    bit_1_of_u_5_8 = u_5_8 & 0b1
    bit_3_of_u_13_16 = (u_13_16 >> 2) & 0b1
    bit_1_of_u_13_16 = u_13_16 & 0b1

    # Extract specific bits from the plaintext
    bit_11_of_plaintext = (plaintext >> 11) & 0b1
    bit_9_of_plaintext = (plaintext >> 9) & 0b1
    bit_8_of_plaintext = (plaintext >> 8) & 0b1

    # Compute the XOR-based linear approximation
    result = (bit_3_of_u_5_8 ^ bit_1_of_u_5_8 ^
              bit_3_of_u_13_16 ^ bit_1_of_u_13_16 ^
              bit_11_of_plaintext ^ bit_9_of_plaintext ^ bit_8_of_plaintext)

    return result
