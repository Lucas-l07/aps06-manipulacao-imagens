import cv2
import numpy as np

img1 = cv2.imread('Images/facil-02-certo.png')
img2 = cv2.imread('Images/facil-02-erro.png')
img5 = img2

alturaImagem01 = img1.shape[0]
alturaImagem02 = img2.shape[0]
larguraImagem01 = img1.shape[1]
larguraImagem02 = img2.shape[1]

text = ''

"----------------------------------------------------"
# Verifica se as dimensões da imagens são iguais
if (alturaImagem01 == alturaImagem02) and (larguraImagem01 == larguraImagem02):
    print("Imagem possuem as mesmas dimensão!")
    for x in range(0, alturaImagem01):
        for y in range(0, larguraImagem01):
            for z in range(0,2):
                img3 = img1[x][y]
                teste4 = img3[z]
                maximo = teste4 + 25
                minimo = teste4 - 25
                if maximo < img2[x][y][z] or img2[x][y][z] < minimo:
                    img5[x][y][0] = 0
                    img5[x][y][1] = 0
                    img5[x][y][2] = 255
                    continue
else:
    print("Imagem com dimensões diferentes!")
"----------------------------------------------------"

# Cor de um pixel
# (b, g, r) = img1[0, 0]
# print("Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

"----------------------------------------------------"

cv2.imshow("img", img5)
cv2.waitKey(0)
cv2.destroyAllWindows()