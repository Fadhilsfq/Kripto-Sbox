import numpy as np
from .helpers import validate_and_pad_sbox

def sbox_to_binary_table(sbox):
    """
    Convert S-Box to binary truth table
    """
    return np.array([[int(bit) for bit in f"{value:08b}"] for value in sbox])

def compute_nonlinearity(sbox):
    """
    Compute the nonlinearity of the S-Box
    """
    # Validate and pad S-box
    sbox = validate_and_pad_sbox(sbox)

    # Convert S-box to binary table (truth table)
    binary_table = sbox_to_binary_table(sbox)
    
    num_inputs = len(sbox)  # Number of possible inputs (usually 256)
    input_bits = int(np.log2(num_inputs))  # Log base 2 of input size to get number of bits
    max_bias = 0  # Initialize maximum bias found

    # Iterate over all non-zero coefficients (coefficients for linear approximation)
    for coeff in range(1, 1 << input_bits):  # Exclude the zero coefficient (no correlation)
        for output_bit in range(8):  # Iterate through each output bit
            biases = []
            for x in range(num_inputs):
                # Calculate dot product between the coefficient and input x
                dot_product = bin(coeff & x).count("1") % 2  # Hamming weight of the coefficient and x
                
                # Get the output bit from the binary table
                output_bit_value = binary_table[x, output_bit]
                
                # Determine the bias based on the comparison of dot product and output bit value
                bias = 1 if dot_product == output_bit_value else -1
                biases.append(bias)
            
            # Calculate total bias for this coefficient and output bit
            total_bias = abs(sum(biases))  # Sum the biases, take the absolute value
            max_bias = max(max_bias, total_bias)  # Track maximum bias found

    # Compute the nonlinearity value
    nonlinearity = (1 << (input_bits - 1)) - (max_bias // 2)  # (2^(n-1)) - (max_bias / 2)
    return nonlinearity