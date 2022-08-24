
from tkinter import Y



class Vecino:
    x=0
    y=0

    posicion=0

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return"%s %s" %(self.x,self.y)
class Coordenada_lectura:
    x=0
    y=0
    def __init__(self, x, y):
        self.x=x
        self.y=y   
       
class Celula:
    
    enferma=False
    
    x=0
    y=0

    posicion=0

    def __init__(self, enferma,x,y,posicion):
        self.enferma=enferma
        self.x=x
        self.y=y
        self.posicion=posicion
    
    #Se usan dos funciones para que el codigo quede más claro
    def enfermar(self):
        self.enferma=True
    
    
    def sanar(self):
        self.enferma=False
    

    def obtenerVecinos(self):
        #Se puede hacer con for pero tu me entiendes
        lista=[]
        vecino1=Vecino(self.x-1, self.y+1)
        vecino2=Vecino(self.x-0, self.y+1)
        vecino3=Vecino(self.x+1, self.y+1)
        vecino4=Vecino(self.x-1, self.y+0)
        vecino5=Vecino(self.x+1, self.y+0)
        vecino6=Vecino(self.x-1, self.y-1)
        vecino7=Vecino(self.x-0, self.y-1)
        vecino8=Vecino(self.x+1, self.y-1)
        
        lista.append(vecino1)
        lista.append(vecino2)   
        lista.append(vecino3)    
        lista.append(vecino4)
        lista.append(vecino5)
        lista.append(vecino6)   
        lista.append(vecino7)
        lista.append(vecino8) 
        return lista
        

        




