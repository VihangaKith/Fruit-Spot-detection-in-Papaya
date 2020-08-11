#Standard imports
import cv2
import numpy as np

#Read image
image = cv2.imread("ringspot.png")
#Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Color strength parameters in HSV
weaker = np.array([0,0,100])
stronger = np.array([10,255,255])

#Threshold HSV image to obtain input color
mask = cv2.inRange(hsv, weaker, stronger)
#Show original image and result
cv2.imshow('Image',image)
cv2.imshow('Result',mask)
#Press any key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
