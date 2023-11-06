import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsLineItem, QGraphicsTextItem, QMainWindow, QWidget, QDesktopWidget, QLabel, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt

class Ventana1(QMainWindow):
    
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)
        
        #Ponemos el titulo
        self.setWindowTitle("Formlario de registro")
        
        #Poner el icono
        
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

         #Imagen de fondo
        self.imagen = QLabel(self)

        self.imagenPantalla = QPixmap("imagenes/fondo.jpg")
                # Establecemos el modo para escalar la imagen
        self.imagen.setPixmap(self.imagenPantalla)

        self.imagen.setScaledContents(True)
        # El tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagen.width(), self.imagen.height())
        # Establecemos la ventana imagen como la ventana central
        self.setCentralWidget(self.imagen)
        
        #Establecemos un layout horizontal
        self.horizontal = QHBoxLayout()
        
        #Establecemos las margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)
        
        
        
        
        
        
        
        # ------------------- PONER AL FINAL --------------------
        
        self.imagen.setLayout(self.horizontal)
        
        
        

    #este if de desición se llama si se ejecuta directamente el archivo
if __name__ == '__main__':
 
 #Hacer que la aplicación se genere   
    app = QApplication(sys.argv)

#Crar un objeto de tipo Ventana1 con el nombre ventana 1
    ventana1 = Ventana1()

#Hacer que el objeto se muestre
    ventana1.show()

    sys.exit(app.exec_())
        
        