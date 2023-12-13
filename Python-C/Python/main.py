import ctypes
import pathlib
import random
import time

def main():
  x = 9
  y = 10
  answer = c_lib.my_sum(x, y)
  print(answer)

def _min(lista):
  #print(lista)
  data = time.time()
  arr = (ctypes.c_int * len(lista))(*lista)
  minimo = c_lib.c_min(arr, len(lista))
  print(minimo)
  print("C", time.time() - data)
  

def py_min(lista):
  #print(lista)
  if(len(lista) > 0):
    minimo = lista[0]
    for i in lista:
      if i < minimo:
        minimo = i
    return minimo
  return 0

def real_min(lista):
  return min(lista)

def merge_sort_c(lista):
  #print(lista)
  data = time.time()
  arr = (ctypes.c_int * len(lista))(*lista)
  c_lib.__mergeSort(arr, 0, len(lista) - 1)
  lista = arr[:]
  data1 = time.time()
  #print(lista)
  print("C mergeSort | tamanho:", len(lista), "tempo:",data1 - data)

def MergeSort(lista, inicio, meio, final):
  start = meio + 1
  if(lista[meio] >= lista[start]):
    while(inicio <= meio and start <= final):
    
      if(lista[inicio] <= lista[start]):
        inicio += 1
      else:
        value = lista[start]
        index = start

        while(index != inicio):
          lista[index] = lista[index - 1]
          index -= 1
        
        lista[inicio] = value

        inicio += 1
        meio += 1
        start += 1
      
    
def merge(lista, inicio, fim):
  if(inicio < fim):
    imed = int(inicio + (fim - inicio)/2)
    merge(lista, inicio, imed)
    merge(lista, imed + 1, fim)

    MergeSort(lista, inicio, imed, fim)
  

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = pathlib.Path().absolute() / "../C/libfunc.so"
    c_lib = ctypes.CDLL(libname)
    main()
    
    lista = [random.randint(-10000, 10000) for _ in range(100000)]
    _min(lista)
    data = time.time()
    print(py_min(lista))
    print("py",time.time() - data)
    
    data = time.time()
    print(real_min(lista))
    print("py min",time.time() - data)

    merge_sort_c(lista)

    #print(lista)
    data = time.time()
    merge(lista, 0, len(lista) - 1)
    data1 = time.time()
    #print(lista)
    print("python merge | tamanho:", len(lista), "tempo:", data1 - data)
