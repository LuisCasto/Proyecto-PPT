from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer
from Logica import JuegoPPT

class JuegoGUI(QWidget):
    def __init__(self, nombre, modo, volver_callback):
        super().__init__()
        self.nombre = nombre
        self.modo = modo
        self.volver_callback = volver_callback
        
        # Inicializar la lógica del juego
        self.juego = JuegoPPT(nombre)
        self.juego.Wins_U = 0
        self.juego.Wins_C = 0
        self.juego.Empates = 0
        
        self.iniciar_juego()

    def iniciar_juego(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Título
        titulo = QLabel(f"🎮 Jugador: {self.nombre} — Modo: {self.modo.upper()}")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        titulo.setStyleSheet("color: white;")
        layout.addWidget(titulo, alignment=Qt.AlignmentFlag.AlignCenter)

        # Marcador
        self.marcador_label = QLabel("👤 Tú: 0 | 🤖 CPU: 0 | 🤝 Empates: 0")
        self.marcador_label.setFont(QFont("Segoe UI", 16))
        self.marcador_label.setStyleSheet("color: #4CAF50; padding: 10px;")
        layout.addWidget(self.marcador_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Puntuación
        self.puntuacion_label = QLabel("📊 Puntuación: 0")
        self.puntuacion_label.setFont(QFont("Segoe UI", 14))
        self.puntuacion_label.setStyleSheet("color: #FFD700;")
        layout.addWidget(self.puntuacion_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Área de resultados
        self.resultado_label = QLabel("🎲 ¡Haz tu jugada!")
        self.resultado_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        self.resultado_label.setStyleSheet("color: white; background-color: #2C2C2C; padding: 20px; border-radius: 10px;")
        self.resultado_label.setWordWrap(True)
        self.resultado_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultado_label)

        # Botones de juego
        botones_layout = QHBoxLayout()
        
        self.piedra_btn = QPushButton("🪨\nPiedra")
        self.papel_btn = QPushButton("📄\nPapel")
        self.tijera_btn = QPushButton("✂️\nTijera")

        botones = [self.piedra_btn, self.papel_btn, self.tijera_btn]
        for i, btn in enumerate(botones, 1):
            btn.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #333;
                    color: white;
                    border-radius: 15px;
                    padding: 20px;
                    min-width: 120px;
                    min-height: 100px;
                }
                QPushButton:hover {
                    background-color: #4CAF50;
                }
                QPushButton:pressed {
                    background-color: #45a049;
                }
            """)
            btn.clicked.connect(lambda checked, jugada=i: self.realizar_jugada(jugada))
            botones_layout.addWidget(btn)

        layout.addLayout(botones_layout)

        # Botón volver
        volver_btn = QPushButton("⬅️ Volver al menú")
        volver_btn.setFont(QFont("Segoe UI", 14))
        volver_btn.setStyleSheet("""
            QPushButton {
                background-color: #444;
                color: white;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)
        volver_btn.clicked.connect(self.volver_callback)
        layout.addWidget(volver_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        self.setStyleSheet("background-color: #1F1F1F;")

    def realizar_jugada(self, jugada_usuario):
        # Deshabilitar botones temporalmente
        self.deshabilitar_botones(True)
        
        # Obtener jugada de la computadora
        if self.modo == "normal":
            jugada_cpu = self.juego.jugada_normal()
        else:
            jugada_cpu = self.juego.jugada_imposible(jugada_usuario)
        
        # Evaluar resultado
        self.juego.evaluar(jugada_usuario, jugada_cpu)
        
        # Mostrar resultado
        jugadas = {1: "🪨 Piedra", 2: "📄 Papel", 3: "✂️ Tijera"}
        
        resultado_texto = f"Tú: {jugadas[jugada_usuario]}\n"
        resultado_texto += f"CPU: {jugadas[jugada_cpu]}\n\n"
        
        if jugada_usuario == jugada_cpu:
            resultado_texto += "🤝 ¡EMPATE!"
            color = "#FFA500"
        elif (jugada_usuario, jugada_cpu) in [(1,3), (2,1), (3,2)]:
            resultado_texto += "🎉 ¡GANASTE ESTA RONDA!"
            color = "#4CAF50"
        else:
            resultado_texto += "💀 PERDISTE ESTA RONDA"
            color = "#F44336"
        
        self.resultado_label.setText(resultado_texto)
        self.resultado_label.setStyleSheet(f"color: white; background-color: {color}; padding: 20px; border-radius: 10px; font-weight: bold;")
        
        # Actualizar marcador
        self.actualizar_marcador()
        
        # Verificar si hay ganador
        QTimer.singleShot(1500, self.verificar_ganador)

    def actualizar_marcador(self):
        self.marcador_label.setText(
            f"👤 Tú: {self.juego.Wins_U} | 🤖 CPU: {self.juego.Wins_C} | 🤝 Empates: {self.juego.Empates}"
        )
        puntos = self.juego.puntuacion()
        self.puntuacion_label.setText(f"📊 Puntuación: {puntos}")

    def verificar_ganador(self):
        if self.juego.Wins_U >= 5:
            self.mostrar_resultado_final("🏆 ¡FELICIDADES! 🏆\n¡Has GANADO la partida!", "#4CAF50")
        elif self.juego.Wins_C >= 5:
            self.mostrar_resultado_final("😢 DERROTA 😢\nLa computadora ganó.\n¡Inténtalo de nuevo!", "#F44336")
        else:
            # Continuar jugando
            self.deshabilitar_botones(False)
            self.resultado_label.setStyleSheet("color: white; background-color: #2C2C2C; padding: 20px; border-radius: 10px;")

    def mostrar_resultado_final(self, mensaje, color):
        self.resultado_label.setText(mensaje)
        self.resultado_label.setStyleSheet(f"color: white; background-color: {color}; padding: 30px; border-radius: 10px; font-size: 24px; font-weight: bold;")
        self.deshabilitar_botones(True)
        
        # Guardar en leaderboard
        puntos = self.juego.puntuacion()
        self.juego.leaderboard(puntos, self.modo)

    def deshabilitar_botones(self, deshabilitar):
        self.piedra_btn.setEnabled(not deshabilitar)
        self.papel_btn.setEnabled(not deshabilitar)
        self.tijera_btn.setEnabled(not deshabilitar)