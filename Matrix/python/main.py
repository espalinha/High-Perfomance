import call_func
import numpy
import time


def test_matrix_c(matrizA, matrizB):
  resultado = call_func.multMatrix(matrizA, matrizB)
  print(resultado)
  print()
  print()
  print()


def mult_matrix(matrizA, matrizB):
  if(matrizA.shape[1] == matrizB.shape[0]):
    MatrizResultado = []

    for i in range(matrizA.shape[0]):
      MatrizResultado.append([])
      for j in range(matrizB.shape[1]):
        soma = 0
        for k in range(matrizB.shape[1]):
          soma += matrizA[i][k] * matrizB[k][j]
        MatrizResultado[i].append(soma)

    #print(MatrizResultado)


def main():
  matrizA = numpy.random.randint(100, size=(1000, 1000))
  matrizB = numpy.random.randint(100, size=(1000, 1000))
  data = time.time()
  test_matrix_c(matrizA, matrizB)
  print(time.time() - data)
  data = time.time()
  mult_matrix(matrizA, matrizB)
  print(time.time() - data)
main()