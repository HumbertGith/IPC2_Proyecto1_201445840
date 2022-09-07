import time
from operator import ge
from tkinter import END, filedialog, messagebox
from celulas import Celula
from lista_pacientes import Lista_pacientes, Nodo_paciente
from metodos import metodos
from paciente import Paciente
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic


#celula:'Celula'
app = QtWidgets.QApplication([])

#cargar ventanas
menu = uic.loadUi("menu.ui")
gestion = uic.loadUi("gestion_usuario.ui")
generar= uic.loadUi("generar_xml.ui")

# se creo la lista
lista=Lista_pacientes()
#objeto de tipo metodos
metodo = metodos
#se carga el archivo xml
def cargar():
       try:
               file = filedialog.askopenfilename(title="abrir", filetypes=(("xml files","*.xml"),("all files", "*.*")))
               metodo.leer_archivo(lista, file)
       except:
               messagebox.showerror("error","El contenido del archivo no es valido o  no has selecionado un archivo")  
menu.setWindowFlag(QtCore.Qt.FramelessWindowHint)
gestion.setWindowFlag(QtCore.Qt.FramelessWindowHint)
generar.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#metodos de navegacion entre ventanas
def cerrar_v():
       menu.close()
def ir_gestion():
       menu.hide()
       gestion.show()
def ir_generar():
       menu.hide()
       generar.show()
def ir_de_gestion_a_menu():
       gestion.hide()
       menu.show()
def ir_de_generar_a_menu():
       generar.hide()
       menu.show()

#metodo para listar los pacientes de forma grafica
def mostrar_pacientes():
   try:
       cadena=lista.listar()
       gestion.textEditpaciente.setPlainText(str(cadena))
   except:
       messagebox.showerror("error","Error al mostral los pacientes")
#metodo para limpiar la muestra de celulas
def limpiar():
   try:
      nombre= gestion.lineEditpaciente.text()
      metodo.limpiar_muestra(lista, nombre)
      cadena=metodo.mostrar_muestra(lista,nombre)
      gestion.textEditmuestra.setPlainText(str(cadena))
   except:
      messagebox.showerror("error","Hubo un error de diseño en la muestra")
#metodo para generar la muestra inicial del paciente
def inicial():
   try:
         gestion.textEditmuestra.setPlainText("")
         nombre= gestion.lineEditpaciente.text()
         metodo.crear_muestra(lista, nombre)
         cadena=metodo.mostrar_muestra(lista, nombre)
         gestion.textEditmuestra.setPlainText(str(cadena))
   except:
         messagebox.showerror("error","Error al generar la muestra inicial")

#metodo para generar los patrones de forma manual 
def manual():
   try:
      gestion.textEditmuestra.setPlainText("")
      nombre= gestion.lineEditpaciente.text()
      cadena=metodo.analizar(lista, nombre)
      gestion.textEditmuestra.setPlainText(str(cadena))

   except:
      messagebox.showerror("error","Error al generar las muestras siguientes de forma manual")

 #metodo para generar los patrones de forma automatica  
def automatico():
   try:
         patron1=""
         nombre= gestion.lineEditpaciente.text()
         metodo.limpiar_muestra(lista, nombre)
         metodo.crear_muestra(lista, nombre)
         patron1=metodo.mostrar_muestra(lista,nombre)
         encontrado= lista.find(nombre)
         if encontrado!= None:
            cadena=""
            patron=""
            encontrado.paciente.listaCe.append(patron1)
           
           
            for i in range(encontrado.paciente.periodo):
               patron=metodo.analizar(lista, nombre)
               encontrado.paciente.listaCe.append(patron)
               cadena=cadena + "Periodo: "+str(i+1)+"\n"+patron+ "\n"
         
            
           
            
            
            gestion.textEditmuestra.setPlainText(str(cadena))
         metodo.mostrar_lista_celulas(lista, nombre)
        



   except:
       messagebox.showerror("error","Error al generar las muestras siguientes de forma automatica")
  

def mostrar_pacientes_genear():
   try:

       cadena=lista.listar()
       generar.textEditpaciente.setPlainText(str(cadena))        
   except:
       messagebox.showerror("error","Error al mostral los pacientes")
  
def generar_xml():
    try:
               configuracion= [('archivos xml', '.xml')]
               f = filedialog.asksaveasfile(filetypes=configuracion, defaultextension=configuracion)
               
     
               nombre= generar.lineEditpaciente.text()
               metodo.escribir_xml(lista,nombre, f)   
               
           
    except:
               messagebox.showerror("error","El contenido del archivo no es valido o  no has selecionado un archivo") 
    
        
         





menu.bt_cargar.clicked.connect(cargar)
menu.bt_cerrar.clicked.connect(cerrar_v)
menu.bt_gestionar.clicked.connect(ir_gestion)
menu.bt_generar.clicked.connect(ir_generar)
#botones gestion
gestion.bt_regresar.clicked.connect(ir_de_gestion_a_menu)
gestion.btnmostrar.clicked.connect(mostrar_pacientes)
gestion.btninicial.clicked.connect(inicial)
gestion.btnmanual.clicked.connect(manual)
gestion.btnlimpiar.clicked.connect(limpiar)
gestion.btnauto.clicked.connect(automatico)
#botones de generar
generar.bt_regresar.clicked.connect(ir_de_generar_a_menu)
generar.btnmostrar.clicked.connect(mostrar_pacientes_genear)
generar.btngenerar.clicked.connect(generar_xml)
menu.show()
app.exec()

