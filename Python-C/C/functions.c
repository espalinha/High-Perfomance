#include <stdio.h>
#include <stdlib.h>

int my_sum(int a, int b)
{
  return a + b;
}

int c_min(int *array, int tam)
{
  if(tam > 0){
    int min = array[0];
    for(int i = 0; i < tam; i++)
    {
      if(array[i] < min) min = array[i];
    }
    return min;
    }
  return 0;
}

void CmergeSort(int *array, int inicio, int meio, int final)
{
    int start = meio + 1;
    if(array[meio] < array[start]) return;
    while(inicio <= meio && start <= final)
    {
      if(array[inicio] <= array[start]) inicio++;
      else{
        int value = array[start];
        int index = start;

        while(index != inicio)
        {
          array[index] = array[index - 1];
          index--;
        }
        array[inicio] = value;

        inicio++;
        meio++;
        start++;
      }
    }
}

void __mergeSort(int *array, int inicio, int fim){
  if(inicio < fim)
  {
    int imed = inicio + (fim - inicio)/2;
    __mergeSort(array, inicio, imed);
    __mergeSort(array, imed + 1, fim);

    CmergeSort(array, inicio, imed, fim);
  }
}