from funcMult import multMatriz, mult_vetor_matriz
import math

class Object:
    def __init__(self, file):
        """Construtor de um objeto. Um arquivo .obj deve ser passado como argumento"""
        self.vertices = []
        self.faces = []
        self.transformacao = [[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]]
        with open(file, 'r') as arquivo:
            for linha in arquivo:
                partes = linha.split()
                if partes[0] == 'v':
                    vertice = list(map(float, partes[1:]))
                    self.vertices.append(vertice)
                elif partes[0] == 'f':
                    vertice = list(map(int, partes[1:]))
                    self.faces.append(vertice)

    