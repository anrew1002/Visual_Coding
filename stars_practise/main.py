import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion,binary_dilation,binary_opening,binary_closing)
from skimage.measure import label

all_im = np.load("stars\stars.npy")
masks = np.array(
   [ [[0,0,1,0,0],
    [0,0,1,0,0],
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0]],
    [[1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1],
     ]
    ]
    )
# all_im = binary_dilation(all_im, mask)
labeled = label(all_im)

def match(a, masks):
    for mask in masks:
        if np.all(a == mask):
            return True
    return False

count = 0
for i in np.unique(labeled)[1:]:
    figure = np.zeros((5,5))
    figure_pos = np.where(labeled == i)
    x_min = min(figure_pos[1])
    y_min = min(figure_pos[0])
    figure = all_im[y_min:y_min+5,x_min:x_min+5]
    if match(figure,masks):
        count+=1

print(count)
plt.imshow(all_im)
# plt.imshow(image, cmap="gray")
plt.show()