import sys

from PyQt5 import QtCore 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QDesktopWidget, QScrollArea, QTableWidget, QTableWidgetItem, QWidget

from PyQt5.QtGui import QColor, QFont, QPixmap,QIcon
from PyQt5.QtCore import Qt
from cliente import Cliente
class Ventana3(QMainWindow):
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Usuarios registrados")

        # Poner el icono
        self.setWindowIcon(QIcon("imagenes\mochila.png"))

        # Establecemos ancho y alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        
        #Hacer que la pantalla se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())
        
        
        # Para que no se pueda mover el tamaño de la ventana
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)
        
         # Imagen de fondo
        self.imagen = QLabel(self)

        self.imagenPantalla = QPixmap("imagenes/fondo.jpg")
        # Establecemos el modo para escalar la imagen
        self.imagen.setPixmap(self.imagenPantalla)

        self.imagen.setScaledContents(True)
        # El tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagen.width(), self.imagen.height())
        # Establecemos la ventana imagen como la ventana central
        self.setCentralWidget(self.imagen)
        
        #Abrimos el archivo en modo lectura
        self.file = open('datos\clientes.txt', 'rb')
        
        #Lista vacia para guardar los usuarios:
        self.usuarios = []
        
        #Recorremos el archivo linea por linea
        
        while self.file:
            linea = self.file.readline().decode("UTF-8")
            
            #Obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            
            #Se para si ya no hay mas registros en el archivo
            if linea == "":
                break
            
            #Creamos un tipo cliente llamado u
            u = Cliente(
                lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9],lista[10])

            #Metemos el objeto en la lista de usuarios
            self.usuarios.append(u)

        #Cerramos el archivo
        self.file.close()
        
        #tenemos la lista usuarios con todos los usuarios
        self.numeroUsuarios = len(self.usuarios)
        
         #Contador de elementos para controlar los usuarios en la tabla
        self.contador = 0
        
        #Establecemos la distrubución de elementos en forma vertical
        self.vertical = QVBoxLayout()
        
        #Hacemos el letrero
        self.letrero1 = QLabel()
        
        #Le escribimos el texto
        self.letrero1.setText("Usuarios registrados")
        
        #Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))
        
        #Le ponemos color de texto y margenes
        self.letrero1.setStyleSheet( "color: #000080;"
        )
        
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()
        
        #Creamos un scroll
        
        self.scrollArea = QScrollArea()
        
        #Hacemos que el scroll se adapte a diferentes tamaños
        
        self.scrollArea.setWidgetResizable(True)
        
        #Creamos una tabla
        self.tabla = QTableWidget()
        
        #Definimos el numero de columnas que tendra la tabla
        self.tabla.setColumnCount(11)
        
        #Definimos el ancho de cada columna
        self.tabla.setColumnWidth(0, 150) 
        self.tabla.setColumnWidth(1, 150) 
        self.tabla.setColumnWidth(2, 150) 
        self.tabla.setColumnWidth(3, 150) 
        self.tabla.setColumnWidth(4, 150) 
        self.tabla.setColumnWidth(5, 150) 
        self.tabla.setColumnWidth(6, 150) 
        self.tabla.setColumnWidth(7, 150) 
        self.tabla.setColumnWidth(8, 150) 
        self.tabla.setColumnWidth(9, 150) 
        self.tabla.setColumnWidth(10, 150)
        
         
        
        #Definimos el texto de la cabecera:
        self.tabla.setHorizontalHeaderLabels(["Nombre Completo",
                                              "Usuario",
                                              "Password",
                                              "Documento",
                                              "Correo",
                                              "Pregunta 1",
                                              "Respuesta 1",
                                              "Pregunta 2",
                                              "Respuesta 2",
                                              "Pregunta 3",
                                              "Respuesta 3"])
        #Establecemos el numero de filas
        self.tabla.setRowCount(self.numeroUsuarios)
        
        #Llenamos la tabla
        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1
            
            #Metemos la tabla en el scroll
            self.scrollArea.setWidget(self.tabla)
            
            #Metemos en el layout vertical el scroll
            self.vertical.addWidget(self.scrollArea)
            
            #Ponemos un espacio despues
            self.vertical.addStretch()
            
            
            
        #---------------------BOTON VOLER---------------------
        
        self.botonVolver = QPushButton("Volver")
        
        #Establecemos el ancho del botón
        self.botonVolver.setFixedWidth(90)
        
        #Le ponemos los estilos
        self.botonVolver.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 10px;")
        
        #Hacemos que el boton volver tenga su metodo:
        self.botonVolver.clicked.connect(self.metodo_botonVolver)
        
        #Lo agregamos al layout
        self.vertical.addWidget(self.botonVolver)
        
#------------------------Ojo ¡PONER AL FINAL! -------------------  #
        self.imagen.setLayout(self.vertical)

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()
          
          
          
          
          
          
if __name__ == "__main__":  
    
    app = QApplication(sys.argv)

        # Crar un objeto de tipo Ventana1 con el nombre ventana 1
    ventana3 = Ventana3()

        # Hacer que el objeto se muestre
    ventana3.show()

    sys.exit(app.exec_())          


         
        