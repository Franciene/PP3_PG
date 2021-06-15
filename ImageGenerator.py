from PIL import Image, ImageColor


def gerar_imagem(cenario, largura, altura):
    im = Image.new('RGB', (largura, altura))  # create the Image of size 1 pixel
    color = ImageColor.getrgb('#634525')

    for objeto in cenario.cena:
        for face in objeto.faces:
            p1_idx, p2_idx, p3_idx = face
            p1 = objeto.vertices[p1_idx - 1]
            p2 = objeto.vertices[p2_idx - 1]
            p3 = objeto.vertices[p3_idx - 1]

            inc_line(im, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), color)
            inc_line(im, int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]), color)
            inc_line(im, int(p1[0]), int(p1[1]), int(p3[0]), int(p3[1]), color)

    im.save('teste.png')  # or any image format


def inc_line(image, x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    inc_e = 2 * dy
    inc_ne = 2 * (dy - dx)
    x = x1
    y = y1
    if x > 0 and y > 0:
        image.putpixel((x, y), color)
    while x < x2:
        if d <= 0:
            d = d + inc_e
            x = x + 1
        else:
            d = d + inc_ne
            x = x + 1
            y = y + 1

        if x > 0 and y > 0:
            image.putpixel((x, y), color)
