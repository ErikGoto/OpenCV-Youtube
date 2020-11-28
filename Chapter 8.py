import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 200:
            cv2.drawContours(imgContour, cnt, -1, (0, 0, 255), 3)
            peri = cv2.arcLength(cnt, True)
            #Função retorna as coordenadas dos contornos
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            #Ao fazer len(approx) descobrimos quantos "vertices" o contorno possui, assim dá pra saber qual a figura geométric
            print(len(approx))
        print(area)


img = cv2.imread("shapes.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

cv2.imshow("Shapes", img)
cv2.imshow("ShapesGray", imgGray)
cv2.imshow("ShapesBlur", imgBlur)
cv2.imshow("ShapesCanny", imgCanny)
cv2.imshow("ShapesContour", imgContour)
cv2.waitKey(0)