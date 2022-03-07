import cv2
import numpy as np
from sys import maxsize


detectarostro = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#DETECTAR SOBRE UNA IMAGEN O FOTO
foto = cv2.imread('diversidad.jpg')

#CAMBIAR A ESCALA DE GRIS
gris = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

#VARIABLE Y FUNCION PARA DETECTAR ROSTROS
caras = detectarostro.detectMultiScale(gris, 
scaleFactor = 1.2, 
minNeighbors = 5, 
minSize = (30,30), 
maxSize=(0,200))

# DIBUJAR LOS ROSTROS DETECTADOS

for (x1,y1,x2,y2) in caras:
    cv2.rectangle(foto, (x1,y1), (x1+x2, y1+y2), (255,255,255),2)

    #MOSTRAR IMAGEN
    cv2.imshow('Imagen detectada', foto)

cv2.waitKey()
cv2.destroyAllWindows()