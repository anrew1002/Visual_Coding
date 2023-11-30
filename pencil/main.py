import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
import numpy as np
from skimage import draw
from skimage.filters import gaussian
from skimage.measure import label, regionprops
import cv2 as cv
import math
from skimage.draw import polygon_perimeter
from skimage.color import rgb2hsv


def search_pencils(labeled_image, min_aspect_ratio=10):
    global globalCounter
    filtered_labeled = np.zeros_like(labeled_image)

    for region in regionprops(labeled_image):
        bbox = region.bbox

        if (region.axis_major_length / region.axis_minor_length) > min_aspect_ratio:
            # print("MATCH!")
            globalCounter += 1
            filtered_labeled[bbox[0]:bbox[2], bbox[1]:bbox[3]
                             ] += region.image

    return filtered_labeled


globalCounter = 0
for i in range(1, 13):

    img = cv.imread(f"images/img ({i}).jpg", cv.IMREAD_GRAYSCALE)

    _, binary_image = cv.threshold(img, 142, 255, cv.THRESH_BINARY_INV)

    kernel = np.ones((3, 3), np.uint8)
    opened_image = cv.morphologyEx(
        binary_image, cv.MORPH_OPEN, kernel, iterations=2)

    closed_image = cv.morphologyEx(
        opened_image, cv.MORPH_CLOSE, kernel, iterations=2)

    labeled = label(closed_image)
    labeled = labeled[50:-50, 50:-50]

    min_object_size = 100
    filtered_labeled = np.where(
        np.isin(labeled, [prop.label for prop in regionprops(labeled) if prop.area >= min_object_size]), labeled, 0)

    pencils_image = search_pencils(filtered_labeled)
    # plt.imshow(pencils_image)
    # plt.show()

print(globalCounter)
