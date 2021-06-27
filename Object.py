from operations import multMatriz, mult_vetor_matriz, product_vetorial, minus_vetorial
import math


class Object:
    def __init__(self, file):
        """Construtor de um objeto. Um arquivo .obj deve ser passado como argumento"""
        self.vertices = []
        self.faces = []
        self.normais = []
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

    def rotacao(self, grau_x=0, grau_y=0, grau_z=0):
        """Expande ou contrai um objeto na cena. Deve ser passado a variação a ser realizada nos eixos."""
        if grau_x != 0:
            seno = math.sin(grau_x * math.pi / 180)
            cosseno = math.cos(grau_x * math.pi / 180)
            matriz = [[1, 0, 0, 0],
                      [0, cosseno, -seno, 0],
                      [0, seno, cosseno, 0],
                      [0, 0, 0, 1]]
            self.transformacao = multMatriz(matriz, self.transformacao)

        if grau_y != 0:
            seno = math.sin(grau_y * math.pi / 180)
            cosseno = math.cos(grau_y * math.pi / 180)
            matriz = [[cosseno, 0, seno, 0],
                      [0, 1, 0, 0],
                      [-seno, 0, cosseno, 0],
                      [0, 0, 0, 1]]
            self.transformacao = multMatriz(matriz, self.transformacao)

        if grau_z != 0:
            seno = math.sin(grau_z * math.pi / 180)
            cosseno = math.cos(grau_z * math.pi / 180)
            matriz = [[cosseno, -seno, 0, 0],
                      [seno, cosseno, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]]
            self.transformacao = multMatriz(matriz, self.transformacao)

    def transformar(self):
        """Aplica a matriz de transformação nos vértices do objeto."""
        self.vertices = list(map(lambda v: mult_vetor_matriz(v + [1], self.transformacao), self.vertices))

    def salvar_objeto(self, file):
        """Construtor de um objeto. Um arquivo .obj deve ser passado como argumento."""
        with open(file, 'w') as arquivo:
            for vertice in self.vertices:
                string = "v {0} {1} {2}\n".format(*vertice)
                arquivo.write(string)
            for face in self.faces:
                string = "f {0} {1} {2}\n".format(*face)
                arquivo.write(string)

    def normal_vertices(self):
        """Retorna todas as normais de cada vértice"""
        # Preciso calcular a normal de cada face
        n = len(self.vertices)
        media = [[0] * n, [0] * n, [0] * n, [0] * n]
        for face in self.faces:
            # Calcula a normal
            v1, v2, v3 = self.vertices[face[0] - 1], self.vertices[face[1] - 1], self.vertices[face[2] - 1]
            normal = product_vetorial(minus_vetorial(v2, v1), minus_vetorial(v3, v1))
            # Soma a normal no acumulado
            media[0][face[0] - 1] = media[0][face[0] - 1] + normal[0]
            media[0][face[1] - 1] = media[0][face[1] - 1] + normal[0]
            media[0][face[2] - 1] = media[0][face[2] - 1] + normal[0]
            media[1][face[0] - 1] = media[1][face[0] - 1] + normal[1]
            media[1][face[1] - 1] = media[1][face[1] - 1] + normal[1]
            media[1][face[2] - 1] = media[1][face[2] - 1] + normal[1]
            media[2][face[0] - 1] = media[2][face[0] - 1] + normal[2]
            media[2][face[1] - 1] = media[2][face[1] - 1] + normal[2]
            media[2][face[2] - 1] = media[2][face[2] - 1] + normal[2]
            # Soma 1 na qtde
            media[3][face[0] - 1] = media[3][face[0] - 1] + 1
            media[3][face[1] - 1] = media[3][face[1] - 1] + 1
            media[3][face[2] - 1] = media[3][face[2] - 1] + 1

        # Depois calcular a normal de cada vértice pela média das faces
        for i in range(n):
            media[0][i] = media[0][i] / media[3][i]
            media[1][i] = media[1][i] / media[3][i]
            media[2][i] = media[2][i] / media[3][i]
        # Então dá para fazer um vetor n por 2 com o acumulado e a quantidade de faces
        self.normais = media[0:3]
