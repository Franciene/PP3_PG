def multMatriz(m1, m2):
    matrizResult = [[0] * 4, [0] * 4, [0] * 4, [0] * 4]

    for i in range(4):
        for j in range(4):
            soma = 0;
            for k in range(4):
                soma += m1[j][k] * m2[k][i];
            matrizResult[j][i] = soma;

    return matrizResult


def mult_vetor_matriz(v, m):
    vetor_result = [0] * 4;

    for j in range(4):
        soma = 0;
        for k in range(4):
            soma += m[j][k] * v[k];
        vetor_result[j] = soma;

    if vetor_result[3] != 1:
        for i in range(4):
            vetor_result[i] = vetor_result[i] / vetor_result[3]

    return vetor_result[0:3]


def product_vetorial(v1, v2):
    result = [0] * 3
    result[0] = v1[1] * v2[2] - v1[2] * v2[1]
    result[1] = v1[2] * v2[0] - v1[0] * v2[2]
    result[2] = v1[0] * v2[1] - v1[1] * v2[0]
    return result


def mult_escalar_vetorial(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]


def division_vetorial(v1, f):
    result = [0] * 3
    result[0] = v1[0] / f
    result[1] = v1[1] / f
    result[2] = v1[2] / f
    return result


def minus_vetorial(v1, v2):
    result = [0] * 3
    result[0] = v1[0] - v2[0]
    result[1] = v1[1] - v2[1]
    result[2] = v1[2] - v2[2]
    return result


def modulo_vetorial(v):
    result = (v[0] ** 2 + v[1] ** 2 + v[2] ** 2) ** 0.5
    return result
