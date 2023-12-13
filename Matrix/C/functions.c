#include <stdio.h>
#include <stdlib.h>

void MatrixMult(size_t row_A, size_t col_A, size_t row_B, size_t col_B,long matrizA[row_A][col_A], long matrizB[row_B][col_B], long matrizC[row_A][col_B])
{
  long soma;
  for(size_t i = 0; i < row_A; i++)
  {
    for(size_t j = 0; j < col_B; j++)
    {
      soma = 0;
      for(size_t k = 0; k < row_B; k++)
      {
        soma += matrizA[i][k] * matrizB[k][j];
      }
      matrizC[i][j] = soma;
    }
  }
}