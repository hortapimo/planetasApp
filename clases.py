import sys
sys.path.append("C:\\Users\\Hortapimo\\OneDrive\\Escritorio\\PEDROR\\PYTHON\\mi_libreria")
import numpy as np


class planeta():
    
    def __init__(self,pos_in_x, pos_in_y, ves_in_x, ves_in_y, masa, nombre):
        self.nombre = nombre
        self.X = np.array([0,0],dtype='float64')
        self.X[0]=pos_in_x
        self.X[1]=pos_in_y
        self.V = np.array([0,0],dtype='float64')
        self.V[0]=ves_in_x
        self.V[1]=ves_in_y
        self.masa = masa
        self.radio = np.cbrt(masa)
        if self.radio < 1:
            self.radio = 1
    
    def actualizar_V(self, delta_t, fuerza):
        self.V = self.V + (fuerza / self.masa ) * delta_t  
            
    def actualizar_X(self, delta_t, fuerza):
        self.actualizar_V(delta_t, fuerza)
        self.X = self.X + self.V * delta_t
        