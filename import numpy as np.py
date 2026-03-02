import multiprocessing
import numpy as np

def multiply_row(args):
    row, B = args
    return np.dot(row, B)

if __name__ == "__main__":
        
    A = np.random.randint(1, 10, (4, 4))
    B = np.random.randint(1, 10, (4, 4))

    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    # Parallel processing
    with multiprocessing.Pool() as pool:
        result = pool.map(multiply_row, [(row, B) for row in A])

    result_matrix = np.array(result)

    print("\nResult Matrix (Parallel):")
    print(result_matrix)