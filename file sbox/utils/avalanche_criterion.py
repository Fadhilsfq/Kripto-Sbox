import numpy as np

def strict_avalanche_criterion(sbox):
    """
    Calculate the Strict Avalanche Criterion (SAC) for an S-box.
    """
    n = 8  # Input and output bit length
    num_inputs = len(sbox)

    # Initialize variables
    total_flips = 0
    total_bits = 0

    # Iterate over all input values
    for input_val in range(num_inputs):
        original_output = binary_representation(sbox[input_val], n)

        # Flip each bit of the input and check the changes in the output
        for bit_to_flip in range(n):
            flipped_input = input_val ^ (1 << bit_to_flip)  # Flip the bit
            flipped_output = binary_representation(sbox[flipped_input], n)

            # Count bit flips in the output using bitwise XOR
            bit_flips = np.sum(np.bitwise_xor(original_output, flipped_output))

            total_flips += bit_flips
            total_bits += n

    # Calculate the SAC value
    sac_value = total_flips / total_bits
    return sac_value

def binary_representation(num, width):
    """Convert number to binary with a fixed width."""
    return [int(x) for x in f"{num:0{width}b}"]