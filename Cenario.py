from operations import product_vetorial, division_vetorial, minus_vetorial, modulo_vetorial, multMatriz


class Cenario:
    def __init__(self):
        self.cena = [];
        self.camera = [[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]]
        self.projecao = [[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]

    def setCamera(self, e, g, t):
        n = division_vetorial(minus_vetorial(g, e), modulo_vetorial(minus_vetorial(g, e)));

        u = division_vetorial(product_vetorial(t, n), modulo_vetorial(product_vetorial(t, n)));

        v = product_vetorial(n, u);

        R = [[*u, 0],
             [*v, 0],
             [*n, 0],
             [0, 0, 0, 1]];
        T = [[1, 0, 0, -e[0]],
             [0, 1, 0, -e[1]],
             [0, 0, 1, -e[2]],
             [0, 0, 0, 1]];
        self.camera = multMatriz(R, T);

    def setProjecao(self):
        pass

    def transforma_cena(self):
        for objeto in self.cena:
            objeto.transformacao = multMatriz(self.camera, objeto.transformacao)
            objeto.transformar()

    def salvar_cenario(self):
        k = 0
        for objeto in self.cena:
            objeto.salvar_objeto('cenario{0}.obj'.format(k))
            k += 1
