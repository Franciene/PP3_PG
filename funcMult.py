def multMatriz(m1, m2):
  matrizResult = [ [0]*4 ] * 4 ;
  for i in range (4):
      for j in range (4):
          soma = 0;
          for k in range (4):
              soma += m1[j][k] * m2[k][j];
          matrizResult[i][j] = soma;
    
  return (matrizResult);    