from celulas import *





    
class Nodo_lectura():
    siguiente: 'Nodo_lectura'
    def __init__(self, lectura):
        self.lectura=lectura
        self.siguiente=None
    def  getSiguiente(self):
          return self.siguiente 
    def setSiguiente(self, siguiente):
          self.siguiente = siguiente  
class Nodo_celula:
    siguiente: 'Nodo_celula'
    #celula: 'Celula'

    def __init__(self,celula: 'Celula') :
         self.celula=celula
         self.siguiente=None
   
        
    def  getSiguiente(self):
          return self.siguiente 
    def setSiguiente(self, siguiente):
          self.siguiente = siguiente  
    