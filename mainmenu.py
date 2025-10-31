import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QVBoxLayout, QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap, QIcon
from juego_gui import JuegoGUI

class PPT(QWidget):
    def __init__(self):
        super().__init__()
        self.incializarjuego()

    def incializarjuego(self):
        self.setGeometry(150,50,1080,720)
        self.setWindowTitle('Piedra, papel o tijera')
        self.setStyleSheet('background-color: #1F1F1F ')
        self.generarmenu()
        self.show()

    def generarmenu(self):
        # Limpiar el layout existente completamente
        if self.layout() is not None:
            QWidget().setLayout(self.layout())
        
        # Crear nuevo layout
        layout = QVBoxLayout()

        label_titulo_img = QLabel()
        pixmap = QPixmap('imagenes/Titulo.png')
        label_titulo_img.setFixedSize(300,300)
        pixmap = pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        label_titulo_img.setPixmap(pixmap)
        
        layout.addWidget(label_titulo_img, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.TAG_label = QLabel(self)
        self.TAG_label.setText('Introduce tu nombre: ')
        self.TAG_label.setFont(QFont("Segoe UI", 23, QFont.Weight.Bold))
        self.TAG_label.setStyleSheet("color: white;")
        layout.addWidget(self.TAG_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.TAG_input = QLineEdit(self)
        self.TAG_input.setFixedWidth(250)
        self.TAG_input.setStyleSheet("""
            QLineEdit {
                font-family: 'Courier New';
                font-size: 20px;
                padding: 10px;
                color: white;
                background-color: #222;
                border: 4px solid blue;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.TAG_input, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.dificultad_label = QLabel(self)
        self.dificultad_label.setText('Haz clic en la dificultad: ')
        self.dificultad_label.setFont(QFont("Segoe UI", 23, QFont.Weight.Bold))
        self.dificultad_label.setStyleSheet("color: white;")
        layout.addWidget(self.dificultad_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        normal_button = QPushButton('Modo normal')
        normal_button.setIcon(QIcon('imagenes/Cara_normal.png'))
        normal_button.setIconSize(QSize(140, 140))
        normal_button.setStyleSheet("""
            QPushButton {
                background-color: #333;
                color: white;
                padding: 10px;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4CAF50;
            }
        """)
        normal_button.clicked.connect(lambda: self.abrirmodo('normal'))
        layout.addWidget(normal_button)

        imposible_button = QPushButton('Modo IMPOSIBLE')
        imposible_button.setIcon(QIcon('imagenes/Cara_imposible.png'))
        imposible_button.setIconSize(QSize(140, 140))
        imposible_button.setStyleSheet("""
            QPushButton {
                background-color: #333;
                color: white;
                padding: 10px;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #F44336;
            }
        """)
        imposible_button.clicked.connect(lambda: self.abrirmodo('imposible'))
        layout.addWidget(imposible_button)
        
        layout.setContentsMargins(20,30,20,30)
        self.setLayout(layout)
        
    def abrirmodo(self, modo):
        nombre = self.TAG_input.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Error", "Por favor, introduce tu nombre primero.")
            return

        # Limpiar el layout actual completamente
        if self.layout() is not None:
            QWidget().setLayout(self.layout())
        
        # Crear nuevo layout para el juego
        layout = QVBoxLayout()
        
        # Crear el juego dentro de la misma ventana
        self.juego_gui = JuegoGUI(nombre, modo, self.generarmenu)
        layout.addWidget(self.juego_gui)
        
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    juego = PPT()
    sys.exit(app.exec())