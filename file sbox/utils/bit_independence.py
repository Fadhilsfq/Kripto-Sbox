import numpy as np
from itertools import product
from .helpers import to_bit_vector, hamming_weight, validate_and_pad_sbox

def calculate_bic_sac(sbox):  
    """  
    Calculate the Bit Independence Criterion - Strict Avalanche Criterion (BIC-SAC)  
    """  
    # Validate and pad S-box
    sbox = validate_and_pad_sbox(sbox)
    
    n = len(sbox)  # Length of S-box (typically 256 for 8-bit S-box)
    total_bits = len(format(n - 1, 'b'))  # Bit length (8 for GF(2^8))  
    bic_sac_values = []  

    # Loop over each bit input and compare different output bits
    for i in range(total_bits):  # Input bit to flip  
        for j1 in range(total_bits):  # First output bit  
            for j2 in range(j1 + 1, total_bits):  # Only check pairs of different output bits
                diff_count = 0  
                for x in range(n):  
                    flipped_x = x ^ (1 << i)  # Flip the i-th input bit  
                    bit_j1 = (sbox[x] >> j1) & 1  # j1 bit of original output  
                    bit_j2 = (sbox[x] >> j2) & 1  # j2 bit of original output  
                    flipped_bit_j1 = (sbox[flipped_x] >> j1) & 1  # j1 bit of flipped output  
                    flipped_bit_j2 = (sbox[flipped_x] >> j2) & 1  # j2 bit of flipped output  
                    # Count the bit differences in both output bits
                    diff_count += (bit_j1 ^ flipped_bit_j1) ^ (bit_j2 ^ flipped_bit_j2)  
                bic_sac_values.append(diff_count / n)  # Normalize for bit pair
    
    # Return the average of all bit pair differences
    return np.mean(bic_sac_values)

def calculate_bic_nl(sbox):  
    """  
    Calculate the Bit Independence Criterion - Nonlinearity (BIC-NL)  
    """  
    # Validate and pad S-box
    sbox = validate_and_pad_sbox(sbox)
    
    n = 8  # Input length (for 8-bit S-box)
    m = 8  # Output length (for 8-bit S-box)
    min_distance = float("inf")  # Start with a large value

    # Convert S-box to boolean function table
    truth_table = np.array([to_bit_vector(sbox[x]) for x in range(256)])

    # Create all affine functions
    affine_masks = list(product([0, 1], repeat=n))  # Generate all possible affine masks (for each input bit)
    
    # Loop over all affine functions
    for mask in affine_masks:  
        mask = np.array(mask)  # Convert mask to numpy array
        for const in [0, 1]:  # For both possible constant values (0 or 1)
            # Generate affine function output for each input
            affine_output = np.array([hamming_weight(mask & to_bit_vector(x)) % 2 ^ const for x in range(256)])
            # Calculate the Hamming distance for all output bits
            for bit in range(m):  # For each output bit
                f_bit = truth_table[:, bit]  # Get the bit for that output
                distance = 256 - np.sum(f_bit == affine_output)  # Calculate Hamming distance
                min_distance = min(min_distance, distance)  # Keep track of the minimum distance

    return min_distance