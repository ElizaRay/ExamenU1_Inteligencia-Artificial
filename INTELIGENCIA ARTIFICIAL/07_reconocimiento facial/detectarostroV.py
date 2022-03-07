import cv2
from sys import maxsize
from tkinter.tix import Tree
from cv2 import VideoCapture
import numpy as np

detectarostro = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#DETECTAR SOBRE VIDEO
cam = cv2.VideoCapture(0)

#CAMBIAR A ESCALA DE GRIS
while True:

    ret,frame = cam.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #VARIABLE Y FUNCION PARA DETECTAR ROSTROS
        caras = detectarostro.detectMultiScale(gris, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30,30), 
        maxSize=(0,200))

# DIBUJAR LOS ROSTROS DETECTADOS

        for (x1,y1,x2,y2) in caras:
            cv2.rectangle(frame, (x1,y1), (x1+x2, y1+y2), (255,255,255),2)

            #MOSTRAR IMAGEN
            cv2.imshow('Imagen detectada', frame)
        
        if cv2.waitKey(1) & 0xFF ==ord('a'):
            break


cam.release()
cv2.destroyAllWindows() 