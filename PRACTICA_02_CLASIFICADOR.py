import cv2
import numpy as np

def clasificador (imagen):
    m,n,c = imagen.shape
    imagen_b=np.zeros((m,n))
    for x in range (m):
        for y in range (n):
            if 50<imagen[x,y,0]<232 and imagen[x,y,1]<232 and imagen[x,y,2]<232:
                imagen_b[x,y]=255
                    
    
    return imagen_b


imagen = cv2.imread("mano.jpg") #se guarda la imagen en la variable imagen
imagen_b = clasificador(imagen)
cv2.imwrite("imagen_b1.jpg",imagen_b)
cv2.imshow("mano binaria",imagen_b)
cv2.imshow("Imagen OG mano", imagen)
cv2.waitKey(0)#espera a aque se presione la X
cv2.destroyAllWindows() #se cierra la ventana al presionar la X