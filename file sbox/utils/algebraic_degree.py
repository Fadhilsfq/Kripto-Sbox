import numpy as np

def compute_algebraic_degree(sbox):
    """
    Menghitung Algebraic Degree dari S-box (n x n).
    Menggunakan Fast Mobius Transform.
    """
    size = len(sbox)
    n = int(np.log2(size)) 
    max_degree = 0
    # Untuk setiap bit output (ada n bit output)
    for bit in range(n):
        truth_table = [(x >> bit) & 1 for x in sbox]
        # Fast Mobius Transform (ANF construction)
        anf = list(truth_table)
        for i in range(n):
            for j in range(size):
                if (j & (1 << i)):
                    anf[j] = (anf[j] + anf[j ^ (1 << i)]) % 2
        
        # Hitung Hamming Weight dari input index dimana ANF bernilai 1
        current_max = 0
        for i in range(size):
            if anf[i] == 1:
                weight = bin(i).count('1')
                if weight > current_max:
                    current_max = weight
        
        if current_max > max_degree:
            max_degree = current_max
    return max_degree
