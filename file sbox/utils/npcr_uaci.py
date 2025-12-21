import numpy as np

def calculate_npcr(img1, img2):
    return np.sum(img1 != img2) / img1.size * 100

def calculate_uaci(img1, img2):
    return np.mean(np.abs(img1.astype(int) - img2.astype(int)) / 255) * 100
