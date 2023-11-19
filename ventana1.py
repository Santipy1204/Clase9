import sys
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsItem,
    QGraphicsLineItem,
    QGraphicsTextItem,
    QMainWindow,
    QWidget,
    QDesktopWidget,
    QLabel,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QLineEdit,
)
from PyQt5.QtGui import QColor, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt


class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # Ponemos el titulo
        self.setWindowTitle("Formlario de registro")

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

        # Establecemos un layout horizontal
        self.horizontal = QHBoxLayout()
        # Establecemos las margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ------------------- Layout izquierda --------------------

        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Información del cliente")
        self.letrero1.setFont(QFont("Andale Mono", 20))
        self.letrero1.setStyleSheet("color : blue;")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(350)
        self.letrero2.setText(
            "Por favor ingrese la información del cliente"
            "\nEn el formulario de abajo los campos marcados"
            "\nLos que estan con asteriscos son obligatorios"
        )
        self.letrero2.setFont(QFont("Andale Mono", 10))
        self.letrero2.setStyleSheet(
            "color: white;"
            "margin-bottom: 20px;"
            "margin-top: 10px;"
            "padding-bottom: 10px;"  # Ajusta el valor según tus necesidades
            "border: 2px solid blue;"
            "border-left: none;"
            "border-right: none;"
            "border-top: none;"
        )
        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombre = QLineEdit()
        self.nombre.setFixedWidth(250)

        self.ladoIzquierdo.addRow(
            '<font color="#FFFFFF">Nombre completo*</font>', self.nombre
        )

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow(
            '<font color="#FFFFFF">Ingrese su usuario*</font>', self.usuario
        )

        self.password = QLineEdit()
        self.password.setFixedWidth(250)

        self.ladoIzquierdo.addRow(
            '<font color="#FFFFFF">Ingrese contraseña*</font>', self.password
        )
        self.password.setEchoMode(QLineEdit.Password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)

        self.ladoIzquierdo.addRow(
            '<font color="#FFFFFF">Vuelva a ingresar la contraseña*</font>',
            self.password2,
        )
        self.password2.setEchoMode(QLineEdit.Password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)

        self.ladoIzquierdo.addRow(
            '<font color="#FFFFFF">Vuelva a ingresar la contraseña*</font>',
            self.password2,
        )

        # Agregamos el layout izquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        # ------------------- PONER AL FINAL --------------------

        self.imagen.setLayout(self.horizontal)

    # este if de desición se llama si se ejecuta directamente el archivo


if __name__ == "__main__":
    # Hacer que la aplicación se genere
    app = QApplication(sys.argv)

    # Crar un objeto de tipo Ventana1 con el nombre ventana 1
    ventana1 = Ventana1()

    # Hacer que el objeto se muestre
    ventana1.show()

    sys.exit(app.exec_())
