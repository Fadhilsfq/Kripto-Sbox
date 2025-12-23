import numpy as np
from Crypto.Cipher import AES

def encrypt_image(img_array, key_bytes, sbox):
    """
    Encrypt image menggunakan AES-128 ECB
    """
    flat = img_array.flatten().astype(np.uint8)
    cipher = AES.new(key_bytes, AES.MODE_ECB)

    pad_len = (16 - len(flat) % 16) % 16
    flat_padded = np.pad(flat, (0, pad_len), mode='constant')

    encrypted = cipher.encrypt(flat_padded.tobytes())
    enc_array = np.frombuffer(encrypted, dtype=np.uint8)[:flat.size]
    
    return enc_array.reshape(img_array.shape)

def decrypt_image(cipher_img, key_bytes, sbox):
    """
    Decrypt image AES (inverse dari encrypt_image)
    """
    flat = cipher_img.flatten().astype(np.uint8)
    cipher = AES.new(key_bytes, AES.MODE_ECB)

    pad_len = (16 - len(flat) % 16) % 16
    flat_padded = np.pad(flat, (0, pad_len), mode='constant')

    decrypted = cipher.decrypt(flat_padded.tobytes())
    dec_array = np.frombuffer(decrypted, dtype=np.uint8)[:flat.size]

    return dec_array.reshape(cipher_img.shape)
