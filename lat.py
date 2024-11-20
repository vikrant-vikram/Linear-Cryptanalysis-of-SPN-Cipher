
from math import trunc, fabs
import itertools as it
import collections
import spn_supplymentary as cipher

def lat():
    # ANSI color codes for terminal output
    RED = '\033[91m'
    RESET = '\033[0m'

    # Generate all 4-bit binary strings
    sbox_in = ["".join(seq) for seq in it.product("01", repeat=4)]

    # Apply the S-box transformation and convert to binary
    sbox_out = [
        bin(int(cipher.sbox[int(seq, 2)], 16))[2:].zfill(4) for seq in sbox_in
    ]

    # Build an ordered dictionary mapping input to output values
    sbox_b = collections.OrderedDict(zip(sbox_in, sbox_out))

    # Initialize the Linear Approximation Table (LAT)
    probBias = [[0 for _ in range(len(sbox_b))] for _ in range(len(sbox_b))]

    # Print header for the LAT
    print("Linear Approximation Table for basic SPN cipher's sbox: ")
    print("(x-axis: output equation - 8, y-axis: input equation - 8)")

    # Perform a complete enumeration of all linear approximations for the SPN cipher's S-box
    for input_bits, output_bits in sbox_b.items():
        # Convert input and output bits from binary to integers
        X1, X2, X3, X4 = [int(bits, 2) for bits in input_bits]
        Y1, Y2, Y3, Y4 = [int(bits, 2) for bits in output_bits]

        # Define all possible linear equations for input and output bits
        equations_in = [
            0, X4, X3, X3 ^ X4, X2, X2 ^ X4, X2 ^ X3, X2 ^ X3 ^ X4, X1, X1 ^ X4,
            X1 ^ X3, X1 ^ X3 ^ X4, X1 ^ X2, X1 ^ X2 ^ X4, X1 ^ X2 ^ X3, X1 ^ X2 ^ X3 ^ X4
        ]

        equations_out = [
            0, Y4, Y3, Y3 ^ Y4, Y2, Y2 ^ Y4, Y2 ^ Y3, Y2 ^ Y3 ^ Y4, Y1, Y1 ^ Y4,
            Y1 ^ Y3, Y1 ^ Y3 ^ Y4, Y1 ^ X2, Y1 ^ Y2 ^ Y4, Y1 ^ Y2 ^ Y3, Y1 ^ Y2 ^ Y3 ^ Y4
        ]

        # Compare input and output equations, and update the probability bias table
        for x_idx in range(len(equations_in)):
            for y_idx in range(len(equations_out)):
                probBias[x_idx][y_idx] += (equations_in[x_idx] == equations_out[y_idx])

    # Print the Linear Approximation Table (LAT) with color
    for bias in probBias:
        for bia in bias:
            # Check if value is non-zero (not zero or '00')
            if bia != 0:
                print(f'{RED}{bia - 8:02d}{RESET}', end=' ')  # Print in red for non-zero
            else:
                print(f'{bia - 8:02d}', end=' ')  # Default color for zero
        print('')

    return probBias
