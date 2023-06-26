from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

# Create your views here.
def entrada_de_datos(request):
  mensaje="Generador de Matrices Numpy"
  return render (request,"formulario.html",locals())


def ejecucion(request):
  if not 'N' in request.GET:
    mensaje = "error de entrada"
    return render(request, "formulario.html", locals())
  
  if request.GET['N']:
    try:
      if int(request.GET['N']) in (2, 3, 4, 5, 6, 7, 8, 9,10):
          
        N = int(request.GET['N'])
        array = np.random.randint(1, 10, (N, N))
        fyc = array.shape
        filas=range(1,fyc[0])
        columnas=fyc[1]
        suma_filas = np.sum(array, axis=1)  # suma filas
        suma_columnas = np.sum(array, axis=0)  # suma columnas
        return render(request,"resultado.html",locals())
      else:
        mensaje="error de entrada"  
        return render(request, "formulario.html", locals())
    except:
        mensaje = "error de entrada"
        return render(request, "formulario.html", locals())
  else:
    mensaje="no has introducido nada"  
    return render(request, "formulario.html", locals())
 