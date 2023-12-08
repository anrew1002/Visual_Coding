import json
import pprint
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2hsv
from skimage.measure import label, regionprops

from collections import defaultdict


dir_path = "balls_and_rects.png"
image = plt.imread(dir_path)
hsv = rgb2hsv(image)
h = hsv[:, :, 0]
image_gray = image.mean(2)
image_binary = (image_gray > 0).astype(np.uint8)
labeled = label(image_binary)

print(f"количество фигур: {np.max(labeled)}")

labeled_regions = regionprops(labeled)
rects_hues = []
circles_hues = []

t_image = np.zeros_like(labeled)

colors_rect = []
colors_circl = []
for region in labeled_regions:

    bbox = region.bbox
    region_image = region.image

    t_image[bbox[0]:bbox[2], bbox[1]:bbox[3]] = region.image

    hue_values = h[bbox[0]:bbox[2], bbox[1]:bbox[3]]

    if region.area == region.area_bbox:
        rects_hues.append('1')
        x,y = region.centroid_local

        colors_rect.append(hue_values[int(x),int(y)])
    else:
        circles_hues.extend('1')
        r = h[bbox[0]:bbox[2], bbox[1]:bbox[3]]
        x,y = region.centroid_local

        colors_circl.append(hue_values[int(x),int(y)])

print(f"количество прямоугольников: {len(rects_hues)}")
print(f"количество кругов: {len(circles_hues)}")


def group_colors(color):
    result = []
    while color:
        color1 = color.pop(0)
        result.append([color1])
        for color2 in color.copy():
            if abs(color1 - color2) < 0.1:
                result[-1].append(color2)
                color.pop(color.index(color2))
    return result


print("круги:")
for group in group_colors(colors_circl):
    
    print(f"Оттенок: {np.average(group)}: {len(group)}")
print("ректы:")
for group in group_colors(colors_rect):
   
    print(f"Оттенок: {np.average(group)}: {len(group)}")

