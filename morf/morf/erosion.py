import matplotlib.pyplot as plt
import numpy as np
from scipy.datasets import face

struct = np.ones((3, 3))


def erosion(arr, mask=struct):
    result = np.zeros_like(arr)
    for y in range(1, arr.shape[0]-1):
        for x in range(1, arr.shape[1]-1):
            sub = arr[y-1:y+2, x-1:x+2]
            if np.all(sub == mask):
                result[y, x] = 1
    return result


if __name__ == '__main__':
    arr = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    res = erosion(arr)
    plt.imshow(res)
    # plt.imshow(arr)
    plt.show()
