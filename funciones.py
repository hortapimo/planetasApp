
from random import randrange
from mis_parametros import *
import clases as c
import numpy as np

def calcular_fuerza(planeta, planetas, delta_t):
    
    distancia=np.array([0,0],dtype='float64')
    fuerza=np.array([0,0],dtype='float64')
    
    for planeta_aux in planetas:
        if (planeta_aux.nombre == planeta.nombre):
            pass
        else:
            distancia = (planeta_aux.X - planeta.X)
            norma =np.sqrt(distancia@distancia)
            if (norma < (planeta.radio + planeta_aux.radio)):
                planeta.V = -planeta.V
                #calcaular bien la conservacion del momento
                
            fuerza += G * ((planeta_aux.masa*planeta.masa)/ (norma**2))*(distancia/norma)
                
    return fuerza
        
def cargar_planetas(planetas, cantidad_planetas):
   j=0
   for i in range(cantidad_planetas):
       planeta = c.planeta(randrange(1,ancho), randrange(1,ancho),
                           randrange(1,ancho), randrange(1,ancho)*0.1,
                           randrange(1,masa_max)*0.1, j)
       j +=1
       planetas.append(planeta)
        
    