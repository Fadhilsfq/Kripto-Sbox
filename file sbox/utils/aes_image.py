import numpy as np
from Crypto.Cipher import AES

def encrypt_image(img_array, key, sbox):
    flat = img_array.flatten()
    cipher = AES.new(key, AES.MODE_ECB)

    pad_len = (16 - len(flat) % 16) % 16
    flat_padded = np.pad(flat, (0, pad_len), mode='constant')

    encrypted = cipher.encrypt(flat_padded.tobytes())
    enc_array = np.frombuffer(encrypted, dtype=np.uint8)[:flat.size]

    return enc_array.reshape(img_array.shape)
