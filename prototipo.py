'''Quiero hacer un juego de piedra papael o tijeras, dos dificultades, una imposible y otra de random, 
quiero que al entrar el usuario se registre con 3 caracteres, habrá un leaderboard para cada dificultad, 
se mostrará al final de cada partida el usuario se registrará solo si sale en el leaderboard, si esntra al 
leaderboard el usuario se actualizará a la lista'''
import random

def evaluar(jugada,contra):

    
    if jugada==contra:
        print('EMPATE')
        return 3
    elif jugada==1 and contra==3:
        print('GANAS')
        return 1
    elif jugada==1 and contra==2:
        print('PIERDES')
        return 2
    elif jugada==2 and contra==1:
        print('GANAS')
        return 1
    elif jugada==2 and contra==3:
        print('PIERDES')
        return 2
    elif jugada==3 and contra==2:
        print('GANAS')
        return 1
    elif jugada==3 and contra==1:
        print('PIERDES')
        return 2
    
def contador_de_wins(Resultado, Wins_U, Wins_C):
    if Resultado == 1:
        Wins_U += 1
    elif Resultado == 2:
        Wins_C += 1
    return Wins_U, Wins_C

    

def seleccionar_dificultad():
    while True:
        print('El ganador será quien gane 5 veces')
        print('Escoge una dificultad')
        print('1..............Normal')
        print('2...........Imposible')
        print('3...............Salir')

        try:
            opc = int(input('Selecciona la dificultad: '))
            if opc in [1, 2, 3]:
                return opc  # Retorna la opción válida y sale del bucle
            else:
                print("Opción no válida. Intenta de nuevo.\n")
        except ValueError:
            print("Error: Debes ingresar un número válido.\n")

def jugada_usuario():
    while True:
        print('Selecciona un número (1.Piedra, 2.Papel, 3.Tijera)')
        try:
            opc = int(input('Tú jugada: '))
            if opc in [1, 2, 3]:
                return opc  # Retorna la opción válida y sale del bucle
            else:
                print("Opción no válida. Intenta de nuevo.\n")
        except ValueError:
            print("Error: Debes ingresar un número válido.\n")

def jugada_normal():
    return random.randint(1, 3)
    
def jugada_imposible(usuario):
    chance=random.randint(0,100)

    if chance<20:
        return random.randint(1, 3)
    else:
        if usuario==1:
            return 2
        elif usuario==2:
            return 3
        elif usuario==3:
            return 1


def modo_normal(Wins_U,Wins_C):
    while True:
        jugada=jugada_usuario()
        if jugada ==1:
            print('Piedra')
        elif jugada==2:
            print('Papel')
        elif jugada==3:
            print('tijeras')
        
        contra=jugada_normal()
        resul=evaluar(jugada,contra)
        Wins_U, Wins_C = contador_de_wins(resul,Wins_U,Wins_C)

        print('MARCADOR: Tú:',Wins_U,'Computadora:',Wins_C)

        if Wins_C==5:
            print('Perdiste la partida! Gana la computadora')
            break
        if Wins_U == 5:
            print('¡Ganaste la partida!')
            break
            
def modo_imposible(Wins_U,Wins_C):
    while True:
        jugada=jugada_usuario()
        if jugada ==1:
            print('Piedra')
        elif jugada==2:
            print('Papel')
        elif jugada==3:
            print('tijeras')
        
        contra=jugada_imposible(jugada)
        resul=evaluar(jugada,contra)
        Wins_U, Wins_C = contador_de_wins(resul,Wins_U,Wins_C)

        print('MARCADOR: Tú:',Wins_U,'Computadora:',Wins_C)

        if Wins_C==5:
            print('Perdiste la partida! Gana la computadora')
            break
        if Wins_U == 5:
            print('¡Ganaste la partida!')
            break

while True:
    Wins_C=0
    Wins_U=0
    print('PPT Lui')

    input("Presiona Enter para continuar...")
    opc = seleccionar_dificultad()

    if opc == 1:
        print("Modo Normal seleccionado.")
        modo_normal(Wins_U,Wins_C)
    elif opc == 2:
        print("Modo Imposible seleccionado.")
        modo_imposible(Wins_U,Wins_C)
    elif opc == 3:
        print("Saliendo del juego...")
        break
    




