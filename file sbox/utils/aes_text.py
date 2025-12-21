from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def format_key(key: str) -> bytes:
    return key.encode().ljust(16, b'\0')[:16]

def encrypt_text(plaintext, key, sbox):
    cipher = AES.new(format_key(key), AES.MODE_ECB)
    ct = cipher.encrypt(pad(plaintext.encode(), 16))
    return base64.b64encode(ct).decode()

def decrypt_text(ciphertext, key):
    cipher = AES.new(format_key(key), AES.MODE_ECB)
    pt = unpad(cipher.decrypt(base64.b64decode(ciphertext)), 16)
    return pt.decode()
