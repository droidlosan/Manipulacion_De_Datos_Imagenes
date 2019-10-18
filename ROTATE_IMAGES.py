from PIL import Image
count=0
total=620
while(count!=total):
	#RUTA DE IMAGEN A ROTAR
	im = Image.open("/home/pi/proyectos/PRUEBA/Recognition/WITH_LIBRARIES_CV/FaceRecognition/ROI_FOTOS2/frame%d.jpg" % count)
	print("%d" %count)
	print( "of %d" %total)
	#GRADOS DE ROTACION
	im = im.rotate(180)
	#GUARDADO DE LA IMAGEN RESULTADO
	im.save("/home/pi/proyectos/PRUEBA/Recognition/WITH_LIBRARIES_CV/FaceRecognition/DERECHO_ROI2/frame%d.jpg" % count)
	count += 1

print("FINISH")
