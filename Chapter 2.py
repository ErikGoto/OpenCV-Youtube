from cv2 import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
img = cv2.imread("urso.png")

imgBlur = cv2.GaussianBlur(img, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("OriginalImage", img)
cv2.imshow("BlurImage", imgBlur)
cv2.imshow("CannyImage", imgCanny)
cv2.imshow("DialationImage", imgDialation)
cv2.imshow("Eroded Image", imgErode)
cv2.waitKey(0)