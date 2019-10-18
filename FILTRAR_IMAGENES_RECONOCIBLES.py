import cv2
import os
import numpy as np
import faceRecognition as fr
from PIL import Image
import glob

#PARTE DE LA DEFINICION DEL NOMBRE
count=0000

#TOTAL DE IMAGENES
total=518

#drectorio de lectura
raiz="/home/pi/proyectos/PRUEBA/Recognition/WITH_LIBRARIES_CV/FaceRecognition/trainingImages/"
#carpeta correspondiente a la coleccion de fotos de tipo 0
ruta= raiz + "0/"

#directorios de resultados
caradetectada="cara_detectada/"
caramarcada="cara_marcada/"

while(count!=total):
	#Leemos la imagen en el directorio predenterminado con su nombre por defecto
	test_img=cv2.imread(ruta + str(count).zfill(5) +".jpg")
	print("%d" %count)
	print( "de %d" %total)
	
	#detectamos las caras de la imagen correspondiente
	faces_detected,gray_img=fr.faceDetection(test_img)
	
	#si detecta imagen devuelve un vector si no, no
	print('faces detected', faces_detected)
	
	#guardamos en diferentes archivos las imagenes detectadas con caras
	#1 sin dibujar el recuadro
	#2 marcando la cara con un recuadro
	# Esto se hace para controlar donde situa la cara y el numero de ellas
	# Util dependiendo si queremos detectar unicamente una cara por imagen
	
	for (x,y,w,h) in faces_detected:
		#1
		cv2.imwrite(ruta + caradetectada + str(count).zfill(5) + ".jpg", test_img)
		cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)
		#2
		cv2.imwrite(ruta + caramarcada + str(count).zfill(5) + ".jpg", test_img)
		
	count += 1

print("FINAL")
