from cv2 import cv2

img = cv2.imread("estrada.png")
print(img.shape)

imgResize = cv2.resize(img, (500, 200))
imgCropped = img[0:100, 200:250]

cv2.imshow("", img)
cv2.imshow("", imgResize)
cv2.imshow("", imgCropped)


cv2.waitKey(0)