
# The Substitution-Permutation Network (SPN) cipher represents a class of symmetric block ciphers. It achieves encryption by repeatedly applying layers of substitution, permutation, and key mixing operations.

# 4.1 Structure Overview

# 	Block Length: lm, where l and m are integers
# 	Substitution :
# S: {0,1}l    {0,1}l, Known as SBOX
# Permutation :
# 	P: {0,1}lm  {0,1}lm, Known as PBOX
# For GPig cipher
# 	l = m = Nr = 4, thus plain text size = 16 bits

# 4.2 SPN encryption:
# Input :
# X : {0,1}lm
# Kr : {0,1}lm
# Output :
# 	Y :  {0,1}lm
# Key schedule :
# 	generates ( K0, ……, KNr)
# W0 = X
# For r = 1 to Nr -1
# 	Ur = Wr-1 Kr-1
# 	For i = 1 to Mr
# 		Vri = S( Uri )
# 	Wr  = Vrp(1)  ,   Vrp(2)  , , ,  Vrp(lm)
# 	UNr =  VNr - 1   KNr - 1
# For i = 1 to m
# 	VNri = S( UNri )
#
#
#
#
import random
import spn_supplymentary as spn_supp
import basic_methods as bm

def key_generator(main_key: str):
    """
    Generate subkeys from the main key for encryption rounds.

    Parameters:
        main_key (str): A 20-character hexadecimal string representing the main key.

    Returns:
        list: A list of 16-bit binary subkeys derived from the main key.
    """
    # Remove spaces from the main key (if any)
    cleaned_key = main_key.replace(" ", "")

    # Split the main key into 5 segments of 4 characters each and convert them to integers
    subkeys = [int(segment, 16) for segment in [cleaned_key[0:4], cleaned_key[4:8],
                                                cleaned_key[8:12], cleaned_key[12:16],
                                                cleaned_key[16:20]]]

    # Convert each subkey to a 16-bit binary string
    return [bin(subkey)[2:].zfill(16) for subkey in subkeys]

def substitution(state: str):
    """
    Apply the substitution step using the S-box.

    Parameters:
        state (str): A 16-bit binary string.

    Returns:
        str: The state after applying substitution.
    """
    substituted_state = ""

    # Iterate over 4-bit chunks in the input state
    for i in range(0, 16, 4):
        # Convert the 4-bit chunk to an integer
        chunk = int(state[i:i+4], 2)

        # Get the S-box substitution value, convert it back to binary, and pad to 4 bits
        substituted_value = bin(int(spn_supp.sbox[chunk], 16))[2:].zfill(4)

        # Append the substituted value to the result
        substituted_state += substituted_value

    return substituted_state

def permutation(state: str):
    """
    Apply the permutation step using the P-box.

    Parameters:
        state (str): A 16-bit binary string.

    Returns:
        str: The state after applying permutation.
    """
    # Rearrange bits in the state according to the P-box
    permuted_state = [state[spn_supp.pbox[i]] for i in range(16)]
    return "".join(permuted_state)

def key_mixing(state: str, key: str):
    """
    Perform the key mixing step using XOR.

    Parameters:
        state (str): A 16-bit binary string.
        key (str): A 16-bit binary subkey.

    Returns:
        str: The state after XOR with the key.
    """
    return bm.xor(state, key)

def encrypt(message: str, main_key: str):
    """
    Encrypt a 16-bit plaintext message using the SPN encryption process.

    Parameters:
        message (str): The plaintext message as a 16-bit binary string.
        main_key (str): The main key as a 20-character hexadecimal string.

    Returns:
        str: The 16-bit encrypted ciphertext.
    """
    # Generate subkeys from the main key
    subkeys = key_generator(main_key)

    # Initialize the state with the plaintext message
    state = message

    # Perform the first 3 rounds of the SPN
    for round_number in range(3):
        # Apply key mixing
        state = key_mixing(state, subkeys[round_number])

        # Apply substitution
        state = substitution(state)

        # Apply permutation
        state = permutation(state)

    # Perform the final round without permutation
    state = key_mixing(state, subkeys[3])
    state = substitution(state)
    state = key_mixing(state, subkeys[4])

    # Return the final ciphertext
    return state
