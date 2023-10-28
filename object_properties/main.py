import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion,binary_dilation,binary_opening,binary_closing)
from skimage.measure import label
from area import area





# image = np.load("wires\wires2.npy")
image = np.zeros((16, 16))
image[4:, :4] = 2

image[3:10, 8:] = 1
image[[3, 4, 3],[8, 8, 9]] = 0
image[[8, 9, 9],[8, 8, 9]] = 0
image[[3, 4, 3],[-2, -1, -1]] = 0
image[[9, 8, 9],[-2, -1, -1]] = 0

image[12:-1, 6:9] = 3

labeled = label(image)
print(area(labeled,1))
print(area(labeled, 2))
print(area(labeled, 3))


plt.imshow(image)
plt.show()