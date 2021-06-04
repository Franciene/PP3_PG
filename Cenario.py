from operations import product_vetorial, division_vetorial, minus_vetorial, modulo_vetorial, multMatriz

class Cenario:
    def __init__():
        self.cena = [];
        self.camera = [];
        self.projecao = [];

    def setCamera(e, g, t):
        n =  division_vetorial( minus_vetorial(g, e), modulo_vetorial(minus_vetorial(g, e))); 
        u =  division_vetorial( product_vetorial(t, n), modulo_vetorial(product_vetorial(t, n)));  
        v =  product_vetorial(n, u);
        R = [[*u, 0],
             [*v, 0],
             [*n, 0],
             [0, 0, 0, 1]];
        T = [[1, 0, 0, -e[0]],
             [0, 1, 0, -e[1]],
             [0, 0, 1, -e[2]],
             [0, 0, 0, 1]];
        self.camera = multMatriz(R, T); 

    def setProjecao():        