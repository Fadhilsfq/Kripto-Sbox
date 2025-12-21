import numpy as np

def binary_representation(num, width):  
    """Convert number to binary with a fixed width."""  
    return [int(x) for x in f"{num:0{width}b}"]  

def to_bit_vector(value, length=8):  
    """Convert a value to a bit vector of specified length"""  
    return np.array([int(x) for x in f"{value:0{length}b}"])  

def hamming_weight(vec):  
    """Calculate the Hamming weight of a vector."""  
    return np.count_nonzero(vec)  # Lebih efisien daripada np.sum()

def validate_and_pad_sbox(sbox):
    """
    Validate and pad/truncate S-box to 256 elements.
    
    Args:
        sbox (list): Input S-box
    
    Returns:
        list: Validated and padded/truncated S-box
    """
    # Salin sbox untuk menghindari perubahan langsung pada input
    sbox = sbox.copy()

    # Pastikan S-box memiliki tepat 256 elemen
    if len(sbox) < 256:
        # Pad dengan nilai 0 jika S-box lebih kecil dari 256 elemen
        sbox.extend([0] * (256 - len(sbox)))
    elif len(sbox) > 256:
        # Potong jika lebih dari 256 elemen
        sbox = sbox[:256]
    
    return sbox