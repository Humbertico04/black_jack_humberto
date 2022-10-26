from random import choice

cartas = {
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
}

lista_cartas = list(cartas)*4

SI = ("s", "si", "y", "yes", "1")

def seleccion_carta():
    """
    Función que elige aleatoriamente una carta y su valor
    """
    carta = choice(lista_cartas)
    score = cartas[carta]
    return carta, score

def entregar_carta(entregas):
    """
    Función que entrega n cartas al usuario
    """
    carta = list(range(entregas))
    score = list(range(entregas))
    for i in range(entregas):
        carta[i], score[i] = seleccion_carta()
    return carta, sum(score)

def mostrar_cartas(usuario, resultado, carta, score):
    """
    Función que muestra al jugador el estado de la partida
    """
    print(usuario, end=" ")
    print(carta, end=" ")
    print(resultado, score)

def pedir_entrada_si_o_no(invitacion):
    """
    Pide al usuario por teclado si desea algo o no
    """
    try:
        return input(invitacion).lower() in SI
    except:
        return False

def sumar_cartas(carta, score):
    """
    Función que añade una carta al usuario
    """
    cartanew, scorenew = entregar_carta(1)
    cartanew += carta
    scorenew += score
    return cartanew, scorenew

def turno_inicial():
    """
    Función para ejecutar el turno 1 del blackjack
    """
    cartasyo, scoreyo = entregar_carta(2)
    cartasia, scoreia = entregar_carta(2)
    return cartasyo, scoreyo, cartasia, scoreia

def empate_derrota(scoreyo, scoreia):
    """
    Funcón que compara los score de ambos participantes y decide si el jugador empate o pierde
    """
    if scoreyo == scoreia:
        print("Empate!")
    else:
        print("Has perdido!")

def lanzador():
    """
    Función que le ofrece al jugador la opción de jugar otra carta y chequea todas las posbilidades del juego
    """
    cartasyo, scoreyo, cartasia, scoreia = turno_inicial()
    while True:
        mostrar_cartas("Ha obtenido:", " >>> su puntuación es de", cartasyo, scoreyo)
        mostrar_cartas("La banca tiene:", " >>> su puntuación es de", cartasia, scoreia)
        if scoreyo == 21 and scoreia != 21:
            print("Blackjack! Has ganado!")
            break
        elif scoreyo > 21:
            print("Has perdido!")
            break
        elif scoreia > 21:
            print("La banca se ha pasado de 21. Has ganado!")
            break
        elif scoreia < 17 <= scoreyo or scoreia < scoreyo <= 17:
            if pedir_entrada_si_o_no("Desea tomar otra carta? ") == True:
                cartasyo, scoreyo = sumar_cartas(cartasyo, scoreyo)
            else:
                cartasia, scoreia = sumar_cartas(cartasia, scoreia)
        elif scoreyo > scoreia:
            if pedir_entrada_si_o_no("Desea tomar otra carta? ") == True:
                cartasyo, scoreyo = sumar_cartas(cartasyo, scoreyo)
            else:
                print("Has ganado!")
                break
        else:
            if pedir_entrada_si_o_no("Desea tomar otra carta? ") == True:
                cartasyo, scoreyo = sumar_cartas(cartasyo, scoreyo)
            else:
                empate_derrota(scoreyo, scoreia)
                break

lanzador()