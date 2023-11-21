import math
import sys

from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QApplication, QScrollArea, QWidget, QGridLayout, \
    QVBoxLayout, QButtonGroup

from cliente import Cliente


class Ventana2(QMainWindow):

    def __init__(self,anterior):
        super(Ventana2,self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Usuarios registrados")

        # Poner el icono
        self.setWindowIcon(QIcon("imagenes\mochila.png"))

        # Establecemos ancho y alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

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

        # Establecemos un layout
        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Usuarios registrados")
        self.letrero1.setFont(QFont("Andale Mono", 20))
        self.letrero1.setStyleSheet("color : blue;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        #creamos un scroll
        self.scrollArea = QScrollArea()

        #lo ponemos transparente
        self.scrollArea.setStyleSheet('background-color: transparent;')

        self.scrollArea.setWidgetResizable(True)

        #crea ventana contenedora para cada celda
        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.vertical.addWidget(self.scrollArea)

        #abrimos el archivo de lectura
        self.file = open('datos/clientes.txt','rb')

        #lista vacia para guardar usuarios
        self.usuarios = []

        #recorremos el archivo, linea por linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            linea = linea.split(';')

            if linea == '':
                break

            #creamos un objeto tipo cliente llamado u
            u = (Cliente( lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9],
                lista[10]))

            self.usuarios.append(u)

        self.file.close()

        #tenemos la lista usuarios con todos los usuarios

        self.numeroUsuarios = len(self.usuarios)

        self.contador = 0

        #definimos la cantidad de elementos para mostrar por columna
        self.elementosPorColumna = 3

        #calculamos el # de filas
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) +1

        #controlamos todos lo botones por variable
        self.botones = QButtonGroup()

        #definimos el controlador de botones
        #debe agrupar a todos lo botones internos
        self.botones.setExclusive(False)




        # ------------------- PONER AL FINAL --------------------

        self.imagen.setLayout(self.vertical)

# Hacer que la aplicación se genere
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crar un objeto de tipo Ventana2 con el nombre ventana 2
    ventana2 = Ventana2()

    # Hacer que el objeto se muestre
    ventana2.show()

    sys.exit(app.exec_())