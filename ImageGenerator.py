from PIL import Image, ImageColor
from operations import multMatriz, mult_vetor_matriz, product_vetorial, minus_vetorial, mult_escalar_vetorial, \
    modulo_vetorial
import math


def gerar_imagem(cenario, largura, altura):
    im = Image.new('RGB', (largura, altura))  # create the Image of size 1 pixel
    colors = [ImageColor.getrgb("hsl(32, 48.2%, 37.8%)"), ImageColor.getrgb("hsl(197, 57.6%, 66.7%)")]

    for i in range(len(cenario.cena)):
        objeto = cenario.cena[i]
        color = colors[i]
        for face in objeto.faces:
            p1_idx, p2_idx, p3_idx = face
            p1 = objeto.vertices[p1_idx - 1]
            p2 = objeto.vertices[p2_idx - 1]
            p3 = objeto.vertices[p3_idx - 1]
            rasteriza_face(im, p1, p2, p3, color)

    im.save('Gato invisível.png')


def rasteriza_face(im, p1, p2, p3, color):
    lista_x = [p1[0], p2[0], p3[0]]
    min_x = int(min(lista_x))

    if min_x < 0:
        min_x = 0

    max_x = int(max(lista_x))

    """0 pro maior, 1 pro menor"""
    lista_y = [[0] * (max_x + 1 - min_x), [math.inf] * (max_x + 1 - min_x)]

    inc_line(im, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), color, lista_y, min_x)
    inc_line(im, int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]), color, lista_y, min_x)
    inc_line(im, int(p3[0]), int(p3[1]), int(p1[0]), int(p1[1]), color, lista_y, min_x)

    for i in range(max_x + 1 - min_x):
        draw_line(im, min_x + i, lista_y[0][i], lista_y[1][i], color)


def inc_line(image, x1, y1, x2, y2, color, lista_y, min_x):
    dx = x2 - x1
    dy = y2 - y1

    fator = max(abs(dx), abs(dy))
    if fator == 0:
        if y1 > lista_y[0][int(x1) - min_x]:
            lista_y[0][int(x1) - min_x] = int(y1)
        if y1 < lista_y[1][int(x1) - min_x]:
            lista_y[1][int(x1) - min_x] = int(y1)
        image.putpixel((int(x1), int(y1)), color)
        return

    inc_x = dx / fator
    inc_y = dy / fator

    x = x1
    y = y1

    while round(x) != x2 or round(y) != y2:
        if int(x) >= 0 and int(y) >= 0:
            if y > lista_y[0][int(x) - min_x]:
                lista_y[0][int(x) - min_x] = int(y)
            if y < lista_y[1][int(x) - min_x]:
                lista_y[1][int(x) - min_x] = int(y)
            image.putpixel((int(x), int(y)), color)
        x = x + inc_x
        y = y + inc_y


def draw_line(image, x, y1, y2, color):
    for i in range(int(abs(y1 - y2)) + 1):
        image.putpixel((int(x), int(y2 + i)), color)


def intensidade_luz(objeto, fonte, intensidade):
    """Retorna um vetor de intensidade de todos os vértices"""
    for normal in objeto.normais:
        coef_difusa = 10
        cos_theta = mult_escalar_vetorial(fonte, normal) / (modulo_vetorial(fonte) * modulo_vetorial(normal))
        difusa = intensidade * coef_difusa * cos_theta


if __name__ == '__main__':
    im = Image.new('RGB', (91, 91))
    rasteriza_face(im, [7, 6], [13, 11], [85, 76], ImageColor.getrgb('#8F6332'))
    im.save('teste.png')
