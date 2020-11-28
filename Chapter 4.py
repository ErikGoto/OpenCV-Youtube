import cv2
import numpy as np

#Uma matriz de zeros representa pixels pretos
img = np.zeros((512, 512, 3), np.uint8)
#Colore a janela
#img[:] = 255, 0, 0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(img, (400, 50), 50, (255, 255, 0), 5)
cv2.putText(img, "Hello", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 150, 0), 1)

cv2.imshow("Janela", img)

cv2.waitKey(0)
