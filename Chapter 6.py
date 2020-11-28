import cv2
import numpy as np

img = cv2.imread("urso.png")
imgResize = cv2.resize(img, (300, 150))

imgHor = np.hstack((imgResize, imgResize))
imgVert = np.vstack((imgResize, imgResize))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVert)
cv2.waitKey(0)