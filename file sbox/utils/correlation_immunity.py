import numpy as np

def fwht(a):
    """Fast Walsh-Hadamard Transform."""
    h = 1
    a = np.array(a, dtype=int)
    while h < len(a):
        for i in range(0, len(a), h * 2):
            for j in range(i, i + h):
                x = a[j]
                y = a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h *= 2
    return a

def compute_correlation_immunity(sbox):
    """
    Menghitung Correlation Immunity order.
    CI order adalah k terbesar dimana Walsh spectrum bernilai 0 
    untuk semua input dengan Hamming weight antara 1 sampai k.
    """
    size = len(sbox)
    n = int(np.log2(size))
    
    min_ci = n 
    # Cek setiap fungsi komponen (kombinasi linear dari bit output)
    # Loop dari 1 sampai 2^n - 1
    for b in range(1, size):
        # Buat fungsi komponen f_b(x) = b dot S(x)
        # Truth table dalam bentuk polarity (+1 / -1)
        f = np.zeros(size, dtype=int)
        for x in range(size):
            dot_val = bin(sbox[x] & b).count('1') % 2
            f[x] = (-1) ** dot_val
        
        # Hitung Walsh Spectrum
        walsh_spec = fwht(f)
        # Cari CI untuk fungsi komponen ini
        # CI adalah k dimana jika 1 <= wt(w) <= k, maka Walsh(w) = 0
        current_ci = n
        for w in range(1, size):
            if walsh_spec[w] != 0:
                hw = bin(w).count('1')
                if hw - 1 < current_ci:
                    current_ci = hw - 1
                    # Optimasi: jika current_ci jadi 0, tidak mungkin lebih rendah
                    if current_ci == 0:
                        break
        
        if current_ci < min_ci:
            min_ci = current_ci
            if min_ci == 0:
                break
                
    return min_ci
