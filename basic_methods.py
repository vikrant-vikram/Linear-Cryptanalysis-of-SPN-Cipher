
import random


def xor(bin_str1, bin_str2):
    """
    Takes two binary strings as input and returns their XOR result as a binary string.

    Args:
    - bin_str1: First binary string.
    - bin_str2: Second binary string.

    Returns:
    - The XOR result of bin_str1 and bin_str2 as a binary string.
    """
    # Perform XOR on each pair of bits
    xor_result = ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(bin_str1, bin_str2))

    return xor_result


def int_to_16bit_binary(num):
    """
    Converts an integer to a 16-bit binary string.

    Args:
    - num: The integer to convert.

    Returns:
    - A 16-bit binary string representation of the integer.
    """
    # Ensure that the number fits within 16 bits and convert to binary
    if num < 0 or num > 65535:
        raise ValueError("The input integer must be between 0 and 65535 (inclusive) to fit within 16 bits.")

    # Convert to binary and remove the "0b" prefix
    bin_str = bin(num)[2:]

    # Pad the binary string to be 16 bits long
    return bin_str.zfill(16)


# def binary_to_integer(bin_str):
#     """
#     Converts a binary string to its integer representation.

#     Args:
#     - bin_str: A string containing a binary number (e.g., '10101').

#     Returns:
#     - The integer representation of the binary string.

#     """

#     # Convert binary string to integer
#     return int(bin_str, 2)
def random_36bit_string()-> str:
    temp = ''.join(random.choice('01') for _ in range(36))
    return temp


def int_to_8bit_binary(num):
    """
    Converts an integer to a 16-bit binary string.

    Args:
    - num: The integer to convert.

    Returns:
    - A 16-bit binary string representation of the integer.
    """
    # Ensure that the number fits within 16 bits and convert to binary
    if num < 0 or num > 65535:
        raise ValueError("The input integer must be between 0 and 65535 (inclusive) to fit within 16 bits.")

    # Convert to binary and remove the "0b" prefix
    bin_str = bin(num)[2:]

    # Pad the binary string to be 16 bits long
    return bin_str.zfill(8)


# def hex_to_binary(hex_string):
#     return bin(int(hex_string, 16))[2:]


def hex_to_binary(hex_string):
    """
    Converts a hexadecimal string to its binary representation.

    Args:
        hex_string (str): The input hexadecimal string.

    Returns:
        str: The binary representation of the hexadecimal string.
    """
    try:
        # Remove any leading "0x" if present
        if hex_string.startswith("0x"):
            hex_string = hex_string[2:]
        # Convert each hex digit to its binary equivalent
        binary_string = bin(int(hex_string, 16))[2:]  # Convert hex to binary and remove "0b"
        # Pad the binary string to ensure it's a multiple of 4 bits
        padded_binary = binary_string.zfill(len(hex_string) * 4)
        return padded_binary
    except ValueError:
       return "Invalid hexadecimal input"


def hex_to_binary_16bit(hex_string):
    """
    Converts a hexadecimal string to a 16-bit binary representation.

    Args:
        hex_string (str): The input hexadecimal string.

    Returns:
        str: A 16-bit binary representation of the hexadecimal string.
    """
    try:
        # Remove any leading "0x" if present
        if hex_string.startswith("0x"):
            hex_string = hex_string[2:]
        # Convert hex to an integer and then to binary, removing "0b"
        binary_string = bin(int(hex_string, 16))[2:]
        # Ensure the binary string is exactly 16 bits long
        padded_binary = binary_string.zfill(8)
        return padded_binary
    except ValueError:
        return "Invalid hexadecimal input"
