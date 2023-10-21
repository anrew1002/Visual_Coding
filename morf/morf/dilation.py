import matplotlib.pyplot as plt
import numpy as np
from scipy.datasets import face

struct = np.ones((3, 3))


def dilation(arr, mask=struct):
    result = np.zeros_like(arr)
    for y in range(1, arr.shape[0] - 1):
        for x in range(1, arr.shape[1] - 1):
            rlog = np.logical_and(arr[y, x], mask)
            result[y - 1:y + 2, x - 1:x + 2] = np.logical_or(result[y - 1:y + 2, x - 1:x + 2], rlog)
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

    res = dilation(arr)
    plt.imshow(res)
    # plt.imshow(arr)
    plt.show()
