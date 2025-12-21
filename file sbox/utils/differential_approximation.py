import numpy as np
from .helpers import validate_and_pad_sbox

def calculate_dap(sbox):
    """
    Calculate Differential Approximation Probability (DAP)
    """
    # Validate and pad S-box
    sbox = validate_and_pad_sbox(sbox)
    
    n = len(sbox)  # S-box length
    max_count = 0  # Variable to store maximum frequency
    
    # Iterate for each input difference (Δx)
    for delta_x in range(1, n):  # Start from 1, as delta_x = 0 is not relevant
        frequency_table = np.zeros(n, dtype=int)  # Frequency table to store Δy counts

        for x in range(n):
            # Calculate y1 and y2 for inputs with Δx difference
            y1 = sbox[x]
            y2 = sbox[x ^ delta_x]  # XOR to get the other input with the difference
            delta_y = y1 ^ y2  # Output difference
            
            # Increment the frequency of the output difference
            frequency_table[delta_y] += 1

        # Find the maximum frequency for all Δy and update max_count
        max_frequency = np.max(frequency_table)
        max_count = max(max_count, max_frequency)  # Track the maximum frequency

    # Calculate DAP (maximum probability)
    dap_value = max_count / n
    return dap_value