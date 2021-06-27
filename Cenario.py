from operations import product_vetorial, division_vetorial, minus_vetorial, modulo_vetorial, multMatriz
import math


class Cenario:
    def __init__(self):
        self.cena = [];

        self.transformacao = [[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]]

    def setCamera(self, e, g, t):
        n = division_vetorial(minus_vetorial(g, e), modulo_vetorial(minus_vetorial(g, e)))
        u = division_vetorial(product_vetorial(t, n), modulo_vetorial(product_vetorial(t, n)))
        v = product_vetorial(n, u)
        R = [[*u, 0],
             [*v, 0],
             [*n, 0],
             [0, 0, 0, 1]]
        T = [[1, 0, 0, -e[0]],
             [0, 1, 0, -e[1]],
             [0, 0, 1, -e[2]],
             [0, 0, 0, 1]]
        self.transformacao = multMatriz(R, T)

    def setProjecao(self, fov, ratio, z_near, z_far):
        tangente = math.sin(fov * math.pi / 180)
        projecao = [[1 / ratio * tangente, 0, 0, 0],
                         [0, 1 / tangente, 0, 0],
                         [0, 0, -(z_far + z_near) / (z_far - z_near), -(2 * z_far * z_near) / (z_far - z_near)],
                         [0, 0, -1, 0]]
        self.transformacao = multMatriz(projecao, self.transformacao)

    def transforma_cena(self):
        for objeto in self.cena:
            objeto.transformar()
            objeto.normal_vertices()
            objeto.transformacao = self.transformacao
            objeto.transformar()

    def translacao(self, offset_x=0, offset_y=0, offset_z=0):
        """Move um objeto na cena. Deve ser passado a variação a ser realizada nos eixos."""
        matriz = [[1, 0, 0, offset_x],
                  [0, 1, 0, offset_y],
                  [0, 0, 1, offset_z],
                  [0, 0, 0, 1]]
        self.transformacao = multMatriz(matriz, self.transformacao)

    def escala(self, prop_x=1, prop_y=1, prop_z=1):
        """Expande ou contrai um objeto na cena. Deve ser passado a variação a ser realizada nos eixos."""
        matriz = [[prop_x, 0, 0, 0],
                  [0, prop_y, 0, 0],
                  [0, 0, prop_z, 0],
                  [0, 0, 0, 1]]
        self.transformacao = multMatriz(matriz, self.transformacao)

    def salvar_cenario(self):
        k = 0
        for objeto in self.cena:
            objeto.salvar_objeto('cenario{0}.obj'.format(k))
            k += 1
