from lista_celulas import Lista_celulas
from lista_lectura import Lista_lectura


class Paciente:
    nombre=""
    edad=0
    periodo=0
    tamanioM=0
    listaCe=[]
    estado1=""
    n=0
  
      
    #lista_celulas:'Lista_celulas'
    def __init__(self, nombre, edad, periodo, tamanioM) :
        self.nombre=nombre
        self.edad=edad
        self.periodo=periodo
        self.tamanioM=tamanioM
        self.lista_celulas=Lista_celulas()
        self.lista_lec=Lista_lectura()
        self.estado1=""
        self.n=0

        
    def  getNombree(self):
          return self.nombre 
    def setNonbre(self, nuevoNombre):
          self.nombre= nuevoNombre
    def  getEdad(self):
          return self.edad 
    def setEdad(self, nuevoEdad):
          self.edad= nuevoEdad
    def  getPeriodo(self):
          return self.periodo 
    def setPeriodo(self, nuevoPeriodo):
          self.periodo= nuevoPeriodo
    def  getMustra(self):
          return self.tamanioM 
    def setMuestra(self, nuevoMuestra):
          self.tamanioM= nuevoMuestra 
    
    def __str__(self):
        return"%s %s" %(self.edad)