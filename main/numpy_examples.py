import numpy as np


def example():
    x = np.array([[1, 2], [3, 4]])  #2x2 matriz
    print(np.sum(x))  # Sum of all elements
    print(np.sum(x, axis=0))  # Sum of each columns
    print(np.sum(x, axis=1))  # Sum of each rows


if __name__ == "__main__":
    example()
