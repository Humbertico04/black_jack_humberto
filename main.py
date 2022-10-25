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

def seleccion_carta():
    """
    Función que elige aleatoriamente una carta y su valor
    """
    carta = choice(lista_cartas)
    score = score = cartas[carta]
    return carta, score

def entregar_carta(entregas):
    """
    Función que entrega n cartas al usuario
    """
    carta = list(range(entregas))
    score = 0
    for i in range(entregas):
        carta[int(i)] = seleccion_carta()[0]
        score += seleccion_carta()[1]
    return carta, score

def mostrar_cartas(usuario, resultado, entregas):
    """
    Función que muestra al jugador el estado de la partida
    """
    carta, score = entregar_carta(entregas)
    print(usuario, end=" ")
    print(carta, end=" ")
    print(resultado, score)
    return carta, score

mostrar_cartas("Ha obtenido:", " >>> su puntuación es de", 2)
mostrar_cartas("La banca tiene:", " >>> su puntuación es de", 2)