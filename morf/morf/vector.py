import matplotlib.pyplot as plt
import numpy as np
from scipy.datasets import face

def translate(image, vector):
    result = np.zeros_like(image)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            ny = y + vector[0]
            nx = x + vector[1]
            if (ny < 0 or nx < 0):
                continue
            elif ny >= image.shape[0] or nx >= image.shape[1]:
                continue
            result[ny, nx] = image[y, x]
    return result

if __name__ == '__main__':
    image = face(True)

    plt.imshow(translate(image, (50, 100)))
    plt.show()