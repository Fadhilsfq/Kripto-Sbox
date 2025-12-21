from .helpers import validate_and_pad_sbox
from collections import defaultdict

def compute_differential_uniformity(sbox):
    """
    Compute the differential uniformity of the S-Box
    """
    # Validate and pad S-box
    sbox = validate_and_pad_sbox(sbox)
    num_inputs = len(sbox)
    max_diff_count = 0

    # Iterate over all input differences (input_diff)
    for input_diff in range(1, num_inputs):  # Start from 1 to skip input_diff = 0 (trivial)
        output_diff_count = defaultdict(int)  # Dictionary to count occurrences of each output_diff

        # Iterate over all input values to compute the output differences
        for x in range(num_inputs):
            y1 = sbox[x]
            y2 = sbox[x ^ input_diff]  # XOR to get the other input value
            output_diff = y1 ^ y2  # XOR to get the output difference
            
            output_diff_count[output_diff] += 1  # Increment the count of this output difference

        # Find the maximum count of any output difference for this input difference
        max_diff_count = max(max_diff_count, max(output_diff_count.values()))

    return max_diff_count