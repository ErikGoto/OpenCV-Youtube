import cv2
import numpy as np

def empty(a):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue min", "TrackBars", 69, 179, empty)
cv2.createTrackbar("Hue max", "TrackBars", 85, 179, empty)
cv2.createTrackbar("Sat min", "TrackBars", 164, 255, empty)
cv2.createTrackbar("Sat max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val min", "TrackBars", 93, 255, empty)
cv2.createTrackbar("Val max", "TrackBars", 255, 255, empty)

cam = cv2.VideoCapture(0)
cam.set(3, 600)
cam.set(4, 600)

while True:
    success, img = cam.read()
    camHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(camHSV, lower, upper)


    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 180, 255), 2)
    cv2.imshow("HSV", camHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Original", img)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
