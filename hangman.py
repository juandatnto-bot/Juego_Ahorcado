"""Archivo principal del juego del ahorcado."""

import random
from palabras import lista_palabras
from monigote import etapas

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    palabra_secreta = random.choice(lista_palabras)

    oculta = []
    for letra in palabra_secreta:
        oculta.append("_")

    usadas = []
    vidas = 6

    print(" ".join(oculta))
    print("Vidas:", vidas)
    print(etapas[0])

    while True:
        letra = input("Ingresa una letra: ")
        letra = letra.upper()
        if len(letra) != 1 or letra not in alfabeto:
            print("Debe ingresar solo 1 letra")
            continue
        if letra in usadas:
            print("Ya ha utilizado la letra")
            continue
        usadas.append(letra)
        if letra in palabra_secreta:
            print("Está")
        else:
            print("No está")
            vidas -= 1
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                oculta[i] = letra
        print(" ".join(oculta))
        print("Vidas:", vidas)
        print(etapas[6 - vidas])
        if "_" not in oculta:
            print("Has adivinado la palabra:", palabra_secreta, "felicidades")
            break
        if vidas == 0:
            print("Has perdido. La palabra era:", palabra_secreta)
            break

    while True:
        opcion = input("¿Quieres jugar de nuevo? (S/N): ")
        opcion = opcion.upper()
        if opcion == "S" or opcion == "N":
            break
        print("Debe ingresar S o N")

    if opcion == "N":
        print("Gracias por jugar")
        break