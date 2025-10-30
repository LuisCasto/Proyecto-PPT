from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

app = QApplication([])

ventana = QWidget()
ventana.setWindowTitle("Botón con imagen")
ventana.setGeometry(100, 100, 300, 200)

boton = QPushButton("Normal", ventana)
boton.setIcon(QIcon("imagenes/Cara_normal.png"))  # Cambia por tu ruta
boton.setIconSize(QSize(100, 100))  # Tamaño del icono (ancho, alto)
boton.move(100, 50)  # Posiciona el botón dentro de la ventana

ventana.show()
app.exec()