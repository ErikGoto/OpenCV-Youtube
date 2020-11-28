import cv2
import numpy as np

def empty(a):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 16, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 73, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 116, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

img = cv2.imread("tomate.png")
imgR = cv2.resize(img, (500,300))
imgHSV = cv2.cvtColor(imgR, cv2.COLOR_BGR2HSV)

while True:
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    #A cor que queremos precisa ficar em branco, e o que não queremos em preto
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(imgHSV, imgR, mask=mask)
    print(h_min, h_max, s_min, s_max, v_min, v_max)


    cv2.waitKey(1)
    cv2.imshow("Original", imgR)
    cv2.imshow("Converted to HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("ImageResult", imgResult)
