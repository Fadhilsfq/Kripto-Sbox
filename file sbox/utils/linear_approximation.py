from .helpers import validate_and_pad_sbox

def linear_approximation_probability(sbox):
    """
    Calculate the Linear Approximation Probability (LAP) for an S-box.
    
    The Linear Approximation Probability measures the correlation between the input 
    and output bits of the S-box. A higher value indicates a less secure S-box.
    """
    # Validate and pad the S-box to ensure it has exactly 256 elements
    sbox = validate_and_pad_sbox(sbox)

    max_lap = 0  # Maximum LAP value found

    # Iterate over all non-zero input and output masks
    for input_mask in range(1, 256):
        for output_mask in range(1, 256):
            count = 0

            # Check all input-output pairs (0 to 255)
            for x in range(256):
                # Calculate input and output parities using bitwise operations
                input_parity = bin(x & input_mask).count('1') % 2  # Parity of the input
                output_parity = bin(sbox[x] & output_mask).count('1') % 2  # Parity of the output

                if input_parity == output_parity:
                    count += 1

            # Calculate the probability for this input/output mask pair and normalize it
            lap = abs(count - 128) / 128  # LAP ranges from 0 to 1
            max_lap = max(max_lap, lap)

    # Normalize the final LAP to 0.5 for cryptographic analysis (range 0 to 0.5)
    return max_lap / 2