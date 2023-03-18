import tkinter as tk
#from controler import Controler
class View:
    def __init__(self, controler):
        
        self.appGUI = tk.Tk()
        self.appGUI.eval('tk::PlaceWindow . center')
        self.splashWindow = tk.Toplevel(self.appGUI)
        self.appGUI.eval(f'tk::PlaceWindow {str(self.splashWindow)} center')
        
        
    def showSplashWindow(self):
        
        self.splashLabel= tk.Label(self.splashWindow, text='Bienvenido a mi Super APP').pack()
        self.splashWindow.geometry("700x500")
        self.splashWindow.attributes('-topmost',True)
        self.splashWindow.overrideredirect(True)
        self.splashWindow.after(3500, self.splashWindow.destroy)
        
    def createGUI(self):
        self.appGUI.title("Simulador de Planetas V2 - Pedro Rabitti")
        self.appGUI.geometry("600x400")
     
        
    def starLoop(self):
        self.appGUI.grab_set()
        self.appGUI.mainloop()
        
    def _splashImage(self):
        
        pass
        
        
