def multMatriz(m1, m2):
    matrizResult = [[0] * 4, [0] * 4, [0] * 4, [0] * 4]

    for i in range(4):
        for j in range(4):
            soma = 0
            for k in range(4):

                soma += m1[j][k] * m2[k][i]
            matrizResult[j][i] = soma

    return matrizResult


def mult_vetor_matriz(v, m):
    vetor_result = [0] * 4

    for j in range(4):
        soma = 0
        for k in range(4):
            soma += m[j][k] * v[k]
        vetor_result[j] = soma

    # if vetor_result[3] != 1:
    #     for i in range(4):
    #         vetor_result[i] = vetor_result[i] / vetor_result[3]

    return vetor_result[0:3]
