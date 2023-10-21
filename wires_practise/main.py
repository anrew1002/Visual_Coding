import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion,binary_dilation,binary_opening,binary_closing)
from skimage.measure import label

image = np.load("wires\wires2.npy")

struct = np.ones((3,1))
labaled=label(image)
# new_image = np.zeros_like(image)
# new_image[labaled==2]=1
# image = binary_erosion(new_image,struct)
# print(np.unique(labaled))
all_im = np.zeros_like(image)
for i in np.unique(labaled)[1:]:
    print(f"for {i} figure:")
    new_image = np.zeros_like(image)
    new_image[labaled==i] = 1
    # zeros = np.zeros_like(image)
    new_image = label(binary_erosion(new_image,struct))
    all_im[new_image > 0] = new_image[new_image > 0]
    print(len(np.unique(new_image))-1)



plt.imshow(all_im)
# plt.imshow(image, cmap="gray")
plt.show()