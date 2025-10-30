from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class JuegoGUI(QWidget):
    def __init__(self, nombre, modo, volver_callback):
        super().__init__()
        self.nombre = nombre
        self.modo = modo
        self.volver_callback = volver_callback  # función para regresar al menú
        self.iniciar_juego()

    def iniciar_juego(self):
        layout = QVBoxLayout()

        # Etiqueta con nombre del jugador y modo
        titulo = QLabel(f"Jugador: {self.nombre} — Modo: {self.modo.upper()}")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        titulo.setStyleSheet("color: white;")
        layout.addWidget(titulo, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botones de juego (piedra, papel, tijera)
        piedra_btn = QPushButton("🪨 Piedra")
        papel_btn = QPushButton("📄 Papel")
        tijera_btn = QPushButton("✂️ Tijera")

        for btn in (piedra_btn, papel_btn, tijera_btn):
            btn.setFont(QFont("Segoe UI", 18))
            btn.setStyleSheet("background-color: #333; color: white; border-radius: 10px; padding: 10px;")
            layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botón para volver al menú
        volver_btn = QPushButton("⬅️ Volver al menú")
        volver_btn.setFont(QFont("Segoe UI", 14))
        volver_btn.setStyleSheet("background-color: #444; color: white; padding: 8px; border-radius: 8px;")
        volver_btn.clicked.connect(self.volver_callback)
        layout.addWidget(volver_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        self.setStyleSheet("background-color: #1F1F1F;")
