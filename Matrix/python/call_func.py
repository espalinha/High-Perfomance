import numpy
import ctypes
import pathlib

def multMatrix(matrizA, matrizB):
  if(matrizA.shape[1] == matrizB.shape[0]): #verify the condition of mult
    libname = pathlib.Path().absolute() / "../C/libfunc.so"
    c_lib = ctypes.CDLL(libname)
    ND_POINTER_2 = numpy.ctypeslib.ndpointer(dtype=numpy.int64, 
                                      ndim=2,
                                      flags="C_CONTIGUOUS") #Here we are telling what type of param we are expectating for the matrices

    c_lib.MatrixMult.argtypes = [ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ND_POINTER_2, ND_POINTER_2, ND_POINTER_2] #Here we are putting how will be all param
    x = matrizA.shape[0] 
    y = matrizB.shape[1]
    MatrizResultado = numpy.zeros((x, y), dtype=numpy.int64)
    c_lib.MatrixMult(*matrizA.shape, *matrizB.shape, matrizA, matrizB, MatrizResultado) #calling the func
    return MatrizResultado
  else:
    return None
