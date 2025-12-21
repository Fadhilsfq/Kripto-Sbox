import numpy as np

def compute_entropy(sbox):  
    """  
    Compute the entropy of the S-box. This includes both the Shannon entropy 
    and the normalized entropy.
    """  
    # Count frequency of each value in S-box
    unique, counts = np.unique(sbox, return_counts=True)
    
    # Calculate probabilities (handle case where count might be zero)
    probabilities = counts / len(sbox)
    
    # Calculate Shannon entropy, with a safeguard against log(0)
    entropy = -np.sum(probabilities * np.log2(probabilities + np.finfo(float).eps))  # Add epsilon to avoid log(0)
    
    # Normalized entropy (between 0 and 1)
    max_possible_entropy = np.log2(len(unique))  # Max entropy for a uniform distribution
    normalized_entropy = entropy / max_possible_entropy  # Normalize the entropy value
    
    return {  
        'shannon_entropy': entropy,  
        'normalized_entropy': normalized_entropy  
    }