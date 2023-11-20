import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout

from PyQt5.QtGui import QColor, QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt
from cliente import Cliente


class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # Ponemos el titulo
        self.setWindowTitle("Formulario de registro")

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
            '<font color="#FFFFFF">Nombre completo*</font>', self.nombre)

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
 
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow(
            '<font color="#FFFFFF">Documento*</font>', self.documento)
        
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow(
            '<font color="#FFFFFF">Correo*</font>', self.correo)
        
        self.BotonRegistrar = QPushButton("Registar")
        self.BotonRegistrar.setFixedWidth(90)
        self.BotonRegistrar.setStyleSheet("background-color: #008B45;"
                                        "color: FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        
        self.BotonRegistrar.clicked.connect(self.accion_BotonRegistrar)
        
        
        self.BotonLimpiar = QPushButton("Limpiar")
        self.BotonLimpiar.setFixedWidth(90)
        self.BotonLimpiar.setStyleSheet("background-color: #008B45;"
                                        "color: FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.BotonLimpiar.clicked.connect(self.accion_BotonLimpiar)
        
        self.ladoIzquierdo.addRow(self.BotonRegistrar, self.BotonLimpiar)

        
        # Agregamos el layout izquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        #layaut DERECHO
        #creamos el layout derecho
        self.ladoDerecho = QFormLayout()

        #asigna margen a la izquierda
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        #hacemos letrero
        self.letrero3 = QLabel()

        self.letrero3.setText('Recuperar contraseña')


        self.letrero3.setFont(QFont("Andale Mono", 20))

        self.letrero3.setStyleSheet('color:#000080')

        #agregamos el letrero
        self.ladoDerecho.addRow(self.letrero3)

        # hacemos letrero
        self.letrero4 = QLabel()

        self.letrero4.setFixedWidth(400)

        self.letrero4.setText('Por favor ingrese la informacion para recuperar'
                       '\nla contraseña. Los campos marcados con asteriscos son obligatorios.')

        self.letrero4.setFont(QFont("Andale Mono", 10))

        self.letrero4.setStyleSheet(
            "color: #000080;"
            "margin-bottom: 40px;"
            "margin-top: 20px;"
            "padding-bottom: 10px;"  # Ajusta el valor según tus necesidades
            "border: 2px solid #000080;"
            "border-left: none;"
            "border-right: none;"
            "border-top: none;")

        # agregamos el letrero
        # agregamos el letrero
        self.ladoDerecho.addRow(self.letrero3)

        #----1

        #hacemos la pregunta 1
        self.labelPregunta1 = QLabel('Pregunta de verificacion 1*')
        self.labelPregunta1.setStyleSheet("color : white;")
        # agregamos
        self.ladoDerecho.addRow(self.labelPregunta1)

        #hacemos el campo para responder
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.pregunta1)

        #hacemos el de respuesta
        self.labelRespuesta1 = QLabel('Respuesta de verificacion 1*')
        self.labelRespuesta1.setStyleSheet("color : white;")
        # agregamos el letrero
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # hacemos el campo para responder
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.respuesta1)

        # ----2

        # hacemos la pregunta \2
        self.labelPregunta2 = QLabel('Pregunta de verificacion 2*')
        self.labelPregunta2.setStyleSheet("color : white;")
        # agregamos
        self.ladoDerecho.addRow(self.labelPregunta2)

        # hacemos el campo para responder
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.pregunta2)

        # hacemos el de respuesta
        self.labelRespuesta2 = QLabel('Respuesta de verificacion 2*')
        self.labelRespuesta2.setStyleSheet("color : white;")
        # agregamos el letrero
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # hacemos el campo para responder
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.respuesta2)

        # ----3

        # hacemos la pregunta 3
        self.labelPregunta3 = QLabel('Pregunta de verificacion 3*')
        self.labelPregunta3.setStyleSheet("color : white;")
        # agregamos
        self.ladoDerecho.addRow(self.labelPregunta3)

        # hacemos el campo para responder
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.pregunta3)

        # hacemos el de respuesta
        self.labelRespuesta3 = QLabel('Respuesta de verificacion 3*')
        self.labelRespuesta3.setStyleSheet("color : white;")
        # agregamos el letrero
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # hacemos el campo para responder
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.respuesta3)

        #hacemos el boton buscar
        self.BotonBuscar = QPushButton("Buscar")
        self.BotonBuscar.setFixedWidth(90)
        self.BotonBuscar.setStyleSheet("background-color: #008B45;"
                                          "color: FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.BotonBuscar.clicked.connect(self.accion_BotonBuscar)

        # hacemos el boton recuperar contraseña
        self.BotonRecuperar = QPushButton("Recuperar")
        self.BotonRecuperar.setFixedWidth(90)
        self.BotonRecuperar.setStyleSheet("background-color: #008B45;"
                                       "color: FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")

        # agregamos los botones
        self.ladoDerecho.addRow(self.BotonBuscar, self.BotonRecuperar)



        #agregamos el layout ladoderecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)


        
        

        # ------------------- PONER AL FINAL --------------------

        self.imagen.setLayout(self.horizontal)

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(300, 150)
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowTitle("Formulario de registro")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)
        self.vertical = QVBoxLayout()

        self.mensaje = QLabel('')
        self.mensaje.setStyleSheet('backgroud-color: #EE6AA7 ; color: #000000 ; padding:10px;')
        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)

        self.ventanaDialogo.setLayout(self.vertical)

        self.datosCorrectos = True

    def accion_BotonLimpiar(self):
        self.nombre.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def accion_BotonRegistrar(self):
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(300,150)
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowTitle("Formulario de registro")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)
        self.vertical = QVBoxLayout()

        self.mensaje = QLabel('')
        self.mensaje.setStyleSheet('backgroud-color: #EE6AA7 ; color: #000000 ; padding:10px;')
        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)

        self.ventanaDialogo.setLayout(self.vertical)

        self.datosCorrectos = True
        if (self.password.text() != self.password2.text()):
            self.datosCorrectos = False

            self.mensaje.setText('Las contraseñas no son iguales')
            self.mensaje.setStyleSheet('backgroud-color: #EE6AA7 ; color:#000000; padding:10px;')

            self.ventanaDialogo.exec_()

        if (
                self.nombre.text() == ''
               or self.usuario.text() == ''
               or self.password.text() == ''
               or self.password2.text() == ''
               or self.documento.text() == ''
               or self.correo.text() == ''
               or self.pregunta1.text() == ''
               or self.respuesta1.text() == ''
               or self.pregunta2.text() == ''
               or self.respuesta2.text() == ''
               or self.pregunta3.text() == ''
               or self.respuesta3.text() == ''
            ):

             
           self.datosCorrectos = False

           self.mensaje.setText('Debe ingresar todos los campos')



           self.ventanaDialogo.exec_()
           
        if  self.datosCorrectos:
            self.file = open('datos/clientes.txt', 'ab')
            # agrega los datos concatenados
            self.file.write(bytes(
                self.nombre.text() + ';'
                + self.usuario.text() + ';'
                + self.password.text() + ';'
                + self.password2.text() + ';'
                + self.documento.text() + ';'
                + self.correo.text() + ';'
                + self.pregunta1.text() + ';'
                + self.respuesta1.text() + ';'
                + self.pregunta2.text() + ';'
                + self.respuesta2.text() + ';'
                + self.pregunta3.text() + ';'
                + self.respuesta3.text() + '\n',
                encoding='UTF-8'))

            self.file.close()

            # Abrimos en modo lectura en formato
            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

    def accion_BotonBuscar(self):
        
        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        if (
            self.documento.text == ''

        ):
            self.datosCorrectos = False

            self.mensaje.setText('Si va a buscar las preguntas para recuperar contraseña debe ingresar el documento')

            self.ventanaDialogo.exec_()

        if (
            not self.documento.text().isnumeric()

        ):
            self.datosCorrectos = False

            self.mensaje.setText('El documento debe ser numerico')

            self.ventanaDialogo.exec_()

            self.documento.setText('')

        if(
            self.datosCorrectos
        ):
            self.file = open('datos/clientes.txt', 'rb')

            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                lista = linea.split(';')
                if linea == '':
                    break
                u = Cliente(
                    lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9],lista[10])

                usuarios.append(u)


            self.file.close()
                
            # En este punto tenemos la lista usuarios con todos los usuarios

            # Variable para controlar si existe el documento:
            existeDocumento = False

            # Buscamos en la lista usuario por usuario si existe la cedula:
            for u in usuarios:
                # comparamos el documento ingresado:
                # si corresponde con el documento, es el usuario correcto:
                if u.documento == self.documento.text():
                    # mostramos las preguntas en el formulario
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)
                    # Indicamos que encontramos el documento
                    existeDocumento = True

                    # Paramos el for
                    break

            # Si no existe un usuario con este documento:
            if (
                        not existeDocumento
            ):
                # Escribimos el texto explicativo:
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                        + self.documento.text())

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()




if __name__ == "__main__":
    # Hacer que la aplicación se genere
    app = QApplication(sys.argv)

    # Crar un objeto de tipo Ventana1 con el nombre ventana 1
    ventana1 = Ventana1()

    # Hacer que el objeto se muestre
    ventana1.show()

    sys.exit(app.exec_())