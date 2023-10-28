import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion,binary_dilation,binary_opening,binary_closing)
from skimage.measure import label
from area import area
from collections import defaultdict


coins = defaultdict(int)
image = np.load("files\coins.npy")
labeled = label(image)
for i in np.unique(labeled)[1:]:
    # print(area(labeled, i))
    coins[int((area(labeled, i)))]+=1

print(coins)
coins_nom = [1,2,5,10]
i = 0
sum_c = 0
for coin_area, k in sorted(coins.items()):
    print(coin_area,k)
    sum_c += k * coins_nom[i]
    i+=1

print(sum_c)
plt.imshow(image)
plt.show()