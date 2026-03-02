import numpy as np # pyright: ignore[reportMissingImports]
import multiprocessing
import time

def hitung_baris(args):
    baris, matriks_b = args
    hasil = []
    for kolom in matriks_b.T:
        total = 0
        for i in range(len(baris)):
            total += baris[i] * kolom[i]
        hasil.append(total)
    return hasil


if __name__ == "__main__":
    n = 500   # bisa diganti sesuai kebutuhan
