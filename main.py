import numpy as np
import matplotlib.pyplot as plt
import random

def buat_labirin(w, h):
    labirin = np.ones((h, w), dtype=int)
    
    def buat_jalur(x, y):
        arah = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(arah)
        
        for dx, dy in arah:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < w and 0 <= ny < h and labirin[ny, nx] == 1:
                labirin[y + dy, x + dx] = 0
                labirin[ny, nx] = 0
                buat_jalur(nx, ny)
    
    labirin[1, 1] = 0
    buat_jalur(1, 1)
    
    labirin[0, 1] = 0  
    labirin[h - 1, w - 2] = 0  
    
    return labirin

def gambar_labirin(labirin):
    plt.figure(figsize=(10, 5))
    plt.imshow(labirin, cmap='binary', interpolation='none')
    
    plt.scatter(1, 0, color='green', s=100, label='Mulai')
    plt.scatter(labirin.shape[1] - 2, labirin.shape[0] - 1, color='red', s=100, label='Keluar')
    
    plt.xticks([])
    plt.yticks([])
    plt.show()

lebar, tinggi = 21, 21 
labirin = buat_labirin(lebar, tinggi)
gambar_labirin(labirin)
