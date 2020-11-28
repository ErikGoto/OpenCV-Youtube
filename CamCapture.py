from cv2 import cv2

cam = cv2.VideoCapture(0)

cam.set(3, 600)
cam.set(4, 400)
cam.set(10, 40)

while True:
    success, img = cam.read()
    imgCanny = cv2.Canny(img, 100, 100)
    cv2.imshow("", imgCanny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break