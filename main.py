
import clases as c
import tkinter
import numpy as np
import funciones as f
from mis_parametros import *

masa_sol = 5000000
masa_tierra = masa_sol/1000000
masa_jupyter = masa_sol/10000

sol = c.planeta(ancho/2, alto/2, 0,0,masa_sol,1)
jupyter = c.planeta(ancho*0.5, alto*0.9, -1.5,-0,masa_jupyter,2)
tierra = c.planeta(ancho*0.3, alto*0.501, 0,-2,masa_tierra,2)
mercurio = c.planeta(ancho*0.37, alto*0.501, 0,-3,masa_tierra/3,2)
marte = c.planeta(ancho*0.35, alto*0.501, 0,-2.5,masa_tierra/2,2)
saturno = c.planeta(ancho*0.2, alto*0.501, 0,-2,masa_jupyter*0.4,2)

planetas = [sol,tierra,jupyter,mercurio,marte,saturno]


# =============================================================================
# planetas = []
# f.cargar_planetas(planetas,50)
# =============================================================================

ventana = tkinter.Tk()
universo = tkinter.Canvas(ventana, width = ancho, height= alto)
universo.pack()
radio = 5
Salir = False
i = 0
tiempo_max = 1,000,000,000 #100 millones
delta_t = 0.1
fuerza = np.array([0,0])


while(Salir == False):
    universo.delete('all')
    i += 1
    for planeta in planetas:
        fuerza = f.calcular_fuerza(planeta, planetas, delta_t)
        planeta.actualizar_X(delta_t, fuerza)
# =============================================================================
#         if((planeta.X[0]>=ancho or planeta.X[0]<= 0) or 
#            (planeta.X[1]>= alto or planeta.X[1]<=0)):
#             planeta.V =planeta.V*(-1)
# =============================================================================
        
        universo.create_oval(planeta.X[0]-planeta.radio,planeta.X[1]-planeta.radio,
                             planeta.X[0]+planeta.radio,planeta.X[1]+planeta.radio, 
                             fill = 'yellow')
    if (i == tiempo_max):
        Salir = True
    universo.update()


ventana.mainloop()