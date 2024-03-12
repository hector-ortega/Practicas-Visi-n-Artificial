import cv2
import numpy as np
imagen = cv2.imread("mano.jpg")
imagenc = imagen.copy()
imageno1 = imagen.copy()
imageno2 = imagen.copy()
# imageno3 = cv2.imread("mano_o3.png")

#184,83,61
#147,98,82
#136,103,89
#119,107,103

m,n,c = imagen.shape



imagen = imagen.astype(np.float32)
#imagenc = imagenc.astype(np.float32)
imageno1 = imageno1.astype(np.float32)
imageno2 = imageno2.astype(np.float32)
# imageno3 = imageno3.astype(np.float32)

def clasificador (imagen,s):
    m,n,c = imagen.shape
    imagen_b=np.zeros((m,n))
    for x in range (m):
        for y in range (n):
            if 50<imagen[x,y,0]<105 and imagen[x,y,1]<110 and imagen[x,y,2]<200:
                imagen_b[x,y]=255
                    

    cv2.imshow(s,imagen_b)
    cv2.imwrite(s+".png",imagen_b)
    return imagen_b

def cromatico(imagenc,s,crom):
    imagen = cv2.imread(s)
    m,n,c = imagen.shape
    imagenc = imagen.copy()
    imagenc = imagenc.astype(np.float32)
    imagen = imagen.astype(np.float32)
    for x in range(m):
        for y in range (n):
            imagenc[x,y,0] = imagen[x,y,0]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
            imagenc[x,y,1] = imagen[x,y,1]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
            imagenc[x,y,2] = imagen[x,y,2]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])

    cv2.imshow(crom,imagenc)
    imagenc = cv2.normalize(imagenc, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite(crom+".png",imagenc)
    return imagenc

#-----------SE CREAN LAS IMAGENES CON DIFERENTE OPACIDAD-----------
imagen = cv2.imread("mano.jpg")
cv2.imshow("mano OG",imagen)

imageno1 = imagen*0.7 #se multiplica por un fator para modificar su nitidez o exposicion
imageno1 = imageno1.astype(np.uint8) #Al multiplicar por el numero flotante se convierte en flotante
cv2.imshow("mano obscura 1",imageno1) #Se muestra la nueva imagen oscura
cv2.imwrite("mano_o1.png",imageno1)

imageno2 = imagen*0.3
imageno2 = imageno2.astype(np.uint8)
cv2.imshow("mano obscura 2",imageno2) #Se muestra la nueva imagen oscura
cv2.imwrite("mano_o2.png",imageno2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#imagen = cv2.imread("mano.jpg") #se guarda la imagen en la variable imagen

imagenc = cromatico(imagenc,"mano.jpg","imagen_cromatica01")
imageno1 = cromatico(imageno1,"mano_o1.png","imagen_cromatica02")
imageno2 = cromatico(imageno2, "mano_o2.png","imagen_cromatica03")
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# imagenc = cv2.imread("imagen_cromatica01.png")
# imageno1 = cv2.imread("imagen_cromatica02.png")
# imageno2 = cv2.imread("imagen_cromatica03.png")

imagenc = clasificador(imagenc,"clasificador_C01")
imageno1 = clasificador(imageno1,"clasificador_C02")
imageno2 = clasificador(imageno2,"clasificador_C03")
cv2.waitKey(0)
cv2.destroyAllWindows()
#espera a aque se presione la X
cv2.destroyAllWindows()

