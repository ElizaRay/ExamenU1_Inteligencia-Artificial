import cv2
import numpy as np

#PARAMETROS COLOR - VENTANA(RESOLUCION VERTICAL, HORIZONTAL, 1) Y EL NUMERADOR
fondo = 255 * np.ones((600,600,3), dtype=np.uint8)

#DIBUJAR UNA LINEA O CUALQUIER FIGURA LOS COLORES ESTAN EN BGR
cv2.line(fondo,(10,10),(590,10),(255,0,255), 2)#linea

cv2.rectangle(fondo,(50,200),(200,300),(0,255,0), 2)#rectangulo

cv2.circle(fondo,(400,300),50,(0,255,255),2)#circulo sin relleno

cv2.circle(fondo,(400,300), 100, (0,255,255), -1)#circulo con relleno

cv2.putText(fondo, 'Open CV1', (10,500), 1, 1, (0,0,0), 2)
cv2.putText(fondo, 'Open CV2', (10,550), 0, 1, (0,0,0), 2)

cv2.imshow("Dibujos", fondo)
cv2.waitKey(0)
cv2.destroyAllWindows(0)