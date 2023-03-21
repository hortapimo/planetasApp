from .view import View

class Controlador:
    def __init__(self):
        self.view = View(self)
    
    def starGUI(self):
        
        self.view.showSplashWindow()
        self.view.createGUI()
        self.view.starLoop()


 
