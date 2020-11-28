from cv2 import cv2 as cv

#Captura as imagens da camera
cam = cv.VideoCapture(0)

#Define as configurações iniciais
#Tamanho da janela
cam.set(3, 640)
cam.set(4, 480)
#Iluminação
cam.set(10, 800)


while True:
    success, img = cam.read()
    cv.imshow("Webcam", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
