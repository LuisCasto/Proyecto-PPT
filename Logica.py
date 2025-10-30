import random

class JuegoPPT:
    def __init__(self, TAG):
        self.TAG = TAG
        self.Wins_U = 0
        self.Wins_C = 0
        self.Empates = 0

    def leaderboard(self, points, modo):
        leaders = []
        leaderboard_path = 'leaderboard_path.txt' if modo == 'normal' else 'leaderboard_path_hard.txt'

        try:
            with open(leaderboard_path, 'a+') as f:
                f.write(f"{self.TAG},{points}\n")
        except:
            pass

        try:
            with open(leaderboard_path, 'r') as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 2:
                        nombre, puntuacion = datos[0], int(datos[1])
                        leaders.append((nombre, puntuacion))

            leaders = sorted(leaders, key=lambda x: x[1], reverse=True)[:10]

            #print("\n🏆 TABLA DE LÍDERES 🏆")
            for i, (nombre, puntuacion) in enumerate(leaders, 1):
                pass
                #print(f"{i}. {nombre} - {puntuacion} puntos")
        except:
            pass
            #print("No se pudo leer el leaderboard.")

    def puntuacion(self):
        return ((self.Wins_U * 100) - (self.Wins_C * 100) + (self.Empates * 25))

    def evaluar(self, jugada, contra):
        resultados = {
            (1, 3): "GANAS",
            (2, 1): "GANAS",
            (3, 2): "GANAS",
        }

        if jugada == contra:
            #print("🤝 ¡Empate! 🤝")
            self.Empates += 1
            return
        elif (jugada, contra) in resultados:
            #print("🎉 ¡Ganaste esta ronda! 🎉")
            self.Wins_U += 1
        else:
            #print("💀 Perdiste esta ronda... 💀")
            self.Wins_C += 1

    def jugada_usuario(self):
        while True:
           #print("Selecciona tu jugada: (1.Piedra, 2.Papel, 3.Tijera)")
            try:
                opc = int(input("Tu jugada: "))
                if opc in [1, 2, 3]:
                    return opc
                else:
                    pass
                    #print("Opción no válida. Intenta de nuevo.\n")
            except ValueError:
                pass
                #print("Error: Debes ingresar un número válido.\n")

    def mostrar_jugada(self, jugada):
        opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras"}
        return opciones.get(jugada, "Desconocido")

    def jugada_normal(self):
        return random.randint(1, 3)

    def jugada_imposible(self, usuario):
        chance = random.randint(0, 100)
        if chance < 20:
            return random.randint(1, 3)
        else:
            return {1: 2, 2: 3, 3: 1}[usuario]

    def jugar(self, modo):
        self.Wins_U = self.Wins_C = self.Empates = 0
        while self.Wins_U < 5 and self.Wins_C < 5:
            jugada = self.jugada_usuario()
            print(f"Tú juegas: {self.mostrar_jugada(jugada)}")

            contra = self.jugada_normal() if modo == "normal" else self.jugada_imposible(jugada)
            print(f"La computadora juega: {self.mostrar_jugada(contra)}")

            self.evaluar(jugada, contra)
            p = self.puntuacion()

            print("\n📊 MARCADOR 📊")
            print(f"👤 Tú: {self.Wins_U} | 🤖 Computadora: {self.Wins_C}")
            print(f"Puntuación: {p}")
            print("----------------------\n")

        if self.Wins_U == 5:
            print("🏆 ¡Felicidades! Has ganado la partida. 🏆")
        else:
            print("😢 La computadora ha ganado. ¡Inténtalo de nuevo! 😢")

        self.leaderboard(p, modo)

    @staticmethod
    def seleccionar_dificultad():
        while True:
            print("\nEl ganador será quien gane 5 veces")
            print("1. Normal")
            print("2. Imposible")
            print("3. Salir")

            try:
                opc = int(input("Selecciona la dificultad: "))
                if opc in [1, 2, 3]:
                    return opc
                else:
                    print("Opción no válida. Intenta de nuevo.\n")
            except ValueError:
                print("Error: Debes ingresar un número válido.\n")


if __name__ == "__main__":
    TAG = input("Ingresa tu nombre: ")
    juego = JuegoPPT(TAG)

    while True:
        print("\n🪨📄✂️  Piedra, Papel o Tijera - By Lui  🪨📄✂️")
        input("Presiona Enter para continuar...")

        opc = juego.seleccionar_dificultad()
        if opc == 1:
            print("\nModo Normal seleccionado.")
            juego.jugar("normal")
        elif opc == 2:
            print("\nModo Imposible seleccionado.")
            juego.jugar("imposible")
        elif opc == 3:
            print("\nSaliendo del juego...")
            break