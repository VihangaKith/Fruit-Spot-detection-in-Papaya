import cv2
import numpy as np
from matplotlib import pyplot as plt

r = tk.Tk()


output_loc = 'D:\\Education\\3rd Year\\3rd Year Project\\Project\\Papaw\\data\\'

try:
    makedirs(output_loc)
except:
    print ("Directory already exist, images will be written in data folder")
r = tk.Tk()


output_loc = 'D:\\Education\\3rd Year\\3rd Year Project\\Project\\Papaw\\data\\'

try:
    makedirs(output_loc)
except:
    print ("Directory already exist, images will be written in data folder")


img = cv2.imread('ringspot.png', cv2.IMREAD_GRAYSCALE)
mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

titles = ['image', 'mask']
images = [img, mask]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

