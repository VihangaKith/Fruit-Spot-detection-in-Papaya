import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = cv2.imread('papaya_ringspot.jpg', 1)
img = cv2.imread('papaya_ringspot.jpg', cv2.IMREAD_GRAYSCALE)
_, mask=cv2.threshold(img, 220, 225, cv2.THRESH_BINARY_INV)

titles = ['Image', 'Gray', 'Mask']
images = [img1, img, mask]


for i in range(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()