import numpy as np

def compute_transparency_order(sbox):
    """
    Menghitung Transparency Order (TO) S-Box 8x8
    berdasarkan definisi Prouff (2005)
    """
    sbox = np.array(sbox)
    n = 8
    N = 256

    to_sum = 0

    for a in range(1, N):
        for b in range(N):
            parity = 0
            for x in range(N):
                y1 = sbox[x]
                y2 = sbox[x ^ a]
                parity += bin(y1 & b).count("1") ^ bin(y2 & b).count("1")
            to_sum += abs(parity)

    return to_sum / ((N - 1) * N * (2 ** n))
