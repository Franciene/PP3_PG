from PIL import Image, ImageColor
from operations import multMatriz, mult_vetor_matriz, product_vetorial, minus_vetorial, mult_escalar_vetorial, \
    modulo_vetorial
import math


def gerar_imagem(cenario, largura, altura):
    im = Image.new('RGB', (largura, altura))  # create the Image of size 1 pixel
    colors = [[32, 48.2], [197, 57.6]]
    # colors = [ImageColor.getrgb("hsl(32, 48.2%, 37.8%)"), ImageColor.getrgb("hsl(197, 57.6%, 66.7%)")]
    fonte = cenario.luz[0:3]
    intensidade = cenario.luz[3]

    for i in range(len(cenario.cena)):
        objeto = cenario.cena[i]
        intensidades = intensidade_luz(objeto, fonte, intensidade)
        color = colors[i]
        for face in objeto.faces:
            p1_idx, p2_idx, p3_idx = face
            p1 = objeto.vertices[p1_idx - 1]
            p2 = objeto.vertices[p2_idx - 1]
            p3 = objeto.vertices[p3_idx - 1]
            rasteriza_face(im, p1, p2, p3, color, intensidades[p1_idx - 1], intensidades[p2_idx - 1], intensidades[p3_idx - 1])

    im.save('Gato invisível.png')


def rasteriza_face(im, p1, p2, p3, color, intensidade1, intensidade2, intensidade3):
    lista_x = [p1[0], p2[0], p3[0]]
    min_x = int(min(lista_x))

    if min_x < 0:
        min_x = 0

    max_x = int(max(lista_x))

    """0 pro maior, 1 pro menor"""
    lista_y = [[0] * (max_x + 1 - min_x),
               [math.inf] * (max_x + 1 - min_x),
               [0] * (max_x + 1 - min_x),
               [0] * (max_x + 1 - min_x)]

    inc_line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), intensidade1, intensidade2, lista_y, min_x)
    inc_line(int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]), intensidade2, intensidade3, lista_y, min_x)
    inc_line(int(p3[0]), int(p3[1]), int(p1[0]), int(p1[1]), intensidade3, intensidade1, lista_y, min_x)

    for i in range(max_x + 1 - min_x):
        draw_line(im, min_x + i, lista_y[0][i], lista_y[1][i], lista_y[2][i], lista_y[3][i], color)


def inc_line(x1, y1, x2, y2, int1, int2, lista_y, min_x):
    dx = x2 - x1
    dy = y2 - y1
    dint = int2 - int1

    fator = max(abs(dx), abs(dy))
    if fator == 0:
        media = (int1 + int2) / 2
        if y1 > lista_y[0][int(x1) - min_x]:
            lista_y[0][int(x1) - min_x] = int(y1)
            lista_y[2][int(x1) - min_x] = int(media)
        if y1 < lista_y[1][int(x1) - min_x]:
            lista_y[1][int(x1) - min_x] = int(y1)
            lista_y[3][int(x1) - min_x] = int(media)
        return

    inc_x = dx / fator
    inc_y = dy / fator
    inc_int = dint / fator

    x = x1
    y = y1
    intens = int1

    while round(x) != x2 or round(y) != y2:
        if int(x) >= 0 and int(y) >= 0:
            if y > lista_y[0][int(x) - min_x]:
                lista_y[0][int(x) - min_x] = int(y)
                lista_y[2][int(x) - min_x] = int(intens)
            if y < lista_y[1][int(x) - min_x]:
                lista_y[1][int(x) - min_x] = int(y)
                lista_y[3][int(x) - min_x] = int(intens)
        x = x + inc_x
        y = y + inc_y
        intens = intens + inc_int


def draw_line(image, x, y1, y2, int1, int2, color):
    if y1 == y2:
        intens = (int1 + int2) / 2
        cor = ImageColor.getrgb("hsl({0}, {1}%, {2}%)".format(color[0], color[1], int(intens)))
        image.putpixel((int(x), int(y1)), cor)
        return

    intens = int1
    inc_intens = (int2 - int1) / abs(y1 - y2)
    for i in range(int(abs(y1 - y2)) + 1):
        cor = ImageColor.getrgb("hsl({0}, {1}%, {2}%)".format(color[0], color[1], int(intens)))
        image.putpixel((int(x), int(y2 + i)), cor)
        intens = intens + inc_intens


def intensidade_luz(objeto, fonte, intensidade):
    """Retorna um vetor de intensidade de todos os vértices"""
    intensidades = []
    for i in range(len(objeto.vertices)):
        normal = [objeto.normais[0][i], objeto.normais[1][i], objeto.normais[2][i]]
        coef_difusa = 0.4
        cos_theta = mult_escalar_vetorial(fonte, normal) / (modulo_vetorial(fonte) * modulo_vetorial(normal))
        difusa = abs(intensidade * coef_difusa * cos_theta)
        intensidades.append(difusa + 10)

    return intensidades


if __name__ == '__main__':
    im = Image.new('RGB', (91, 91))
    rasteriza_face(im, [7, 6], [13, 11], [85, 76], ImageColor.getrgb('#8F6332'))
    im.save('teste.png')
