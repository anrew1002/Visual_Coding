import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops


points = []
x_first, y_first, x_second, y_second = [], [], [], []

for i in range(100):
    image = np.load(f"out/h_{i}.npy")
    labeled = label(image)

    regions = sorted(regionprops(label(image)), key=lambda region: region.area)

    (y1, x1) = regions[0].centroid
    (y2, x2) = regions[1].centroid

    x_first.append(x1)
    y_first.append(y1)
    x_second.append(x2)
    y_second.append(y2)

plt.plot(x_first, y_first)
plt.plot(x_second, y_second)
plt.legend()
plt.show()

