import filecmp
from os import listdir

def ls(ruta = '.'):
    return listdir(ruta)

#ANTERIORMENTE LAS IMAGENES MARCADAS CON CARA TUVO QUE HABER PASADO UN RECONOCIMIENTO MANUAL
#Y HABER BORRADO EL FILTRADO MANUAL, POR EJEMPLO QUE TENGA MAS DE UNA CARA

#RUTA IMAGENES PARA FILTRAR
dir1="/home/pi/proyectos/PRUEBA/Recognition/WITH_LIBRARIES_CV/FaceRecognition/FERNANDO_c"
#RUTA IMAGENES CONFIRMADAS CON CARA
dir2="/home/pi/proyectos/PRUEBA/Recognition/WITH_LIBRARIES_CV/FaceRecognition/FERNANDO_RET"

archivos1= ls(dir1)
print(archivos1)
archivos2=ls(dir2)
print(archivos2)

#INDICA FICHEROS A BORRAR
BORRAR=list(set(archivos1) - set(archivos2))
print("BORRAR: ", BORRAR)

