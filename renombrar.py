import os
import glob

originales=[]
def devolverArchivos(carpeta):
	originales=[]
	i=0
	for archivo in os.listdir(carpeta):
		originales.append(os.path.join(carpeta,archivo))
		i=i+1
		print(archivo)
		#print("Archivo: ",i)
	print ("Numero de archivos totales: ",i-1)
	return originales
	
#RUTA DE LA CARPETA A CAMBIAR NOMBRES DE LOS ARCHIVOS O IMAGENES	
ruta="/home/pi/proyectos/PRUEBA/Recognition/WITH_LIBRARIES_CV/FaceRecognition/trainingImages/0"	
#FUNCION QUE DEVUELVE LA LISTA ACTUAL Y EL NUMERO DE ARCHIVOS
originales=devolverArchivos(ruta)

identificador = 0
#CREAMOS OTRA LISTA DE SOLO IMAGENES Y MOSTRAMOS POR PANTALLA
lista_fotos = sorted(glob.glob(ruta + '/*.jpg'))
print(lista_fotos)
#CAMBIAMOS EL NOMBRE DE LAS IMAGENES
#IMPORTANTE: EN CADA EJECUCION DEL PROGRAMA SE HA DE PONER UN NUEVO NOMBRE 
# PARA LA MISMA CARPETA,SI NO PUEDE BORRAR ARCHIVOS DE MANERA ACCIDENTAL
for i in lista_fotos:   
    nuevo_nombre = ruta + '/' + 'FERNANDO' + str(identificador).zfill(5) +'.jpg'        
    identificador = identificador + 1
    os.rename(i, nuevo_nombre)
    print('cambio')
print('ACABE')

