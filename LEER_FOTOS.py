##LEER FOTOS
import cv2
import os
import numpy as np
import faceRecognition as fr

#RUTA DE LA IMAGEN A LEER LAS CARAS
test_img = cv2.imread('/home/pi/proyectos/PRUEBA/Recognition/WITH_LIBRARIES_CV/FaceRecognition/FOTOS_INSTA_DUONG/Screenshot_20191017-022303.jpg')

#SE APLICA LA LECTURA Y SE DEVUELVE EL VECTOR
faces_detected,gray_img=fr.faceDetection(test_img)
print('faces detected', faces_detected)
#MARCAR LAS CARAS DETECTADAS
for (x,y,w,h) in faces_detected:
	cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)
	
resized_img=cv2.resize(test_img,(1000,700))
cv2.imshow("face detection tutorial", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows




