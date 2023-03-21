import tkinter as tk

class View:
    def __init__(self, controlador):
        
        self.appGUI = tk.Tk()
        self.appGUI.eval('tk::PlaceWindow . center')
        self.splashWindow = tk.Toplevel(self.appGUI)
        self.appGUI.eval(f'tk::PlaceWindow {str(self.splashWindow)} center')
        self.controlador = controlador
        
        
    def showSplashWindow(self):
        
        self.splashLabel= tk.Label(self.splashWindow, text='Bienvenido a mi Super APP').pack()
        self.splashWindow.geometry("1000x500")
        self.splashWindow.attributes('-topmost',True)
        self.splashWindow.overrideredirect(True)
        self.splashWindow.after(3500, self.splashWindow.destroy)
        
    def createGUI(self):
        self.appGUI.title("Simulador de Planetas V2 - Pedro Rabitti")
        self.appGUI.geometry("600x400")
        self.ventanaInicio = tk.Frame()
        self.ventanaInicio.pack()
        instruccionesTxt = open("instrucciones.txt",'r')
        self.intrucciones = tk.Label(self.ventanaInicio,text=instruccionesTxt.read())
        self.intrucciones.pack(pady=30)
        self.botonSiguiente = tk.Button(self.ventanaInicio, text="Siguiente",command= self.controlador.botonSiguiente)
        self.botonSiguiente.pack()

    def crearVentanaCargaDeDatos(self):
        self.ventanaInicio.destroy()
        self.ventanaDatos = tk.Frame()
        self.ventanaDatos.pack()

        self.cantidadPlanetas = tk.Label(self.ventanaDatos, text="Cantidad de planetas:")
        self.cantidadPlanetas.pack()
        self.rtaCantidadPlanetas = tk.Entry()
        self.rtaCantidadPlanetas.pack()


        
     
        
    def starLoop(self):
        self.appGUI.grab_set()
        self.appGUI.mainloop()
        
    def _splashImage(self):
        
        pass
        
        
