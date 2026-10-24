"""Archivo principal del juego del ahorcado."""

import random 
from palabras import lista_palabras


palabra_secreta = random.choice(lista_palabras)

oculta = []
for letra in palabra_secreta:
    oculta.append("_")

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    letra = input("Ingresa una letra: ")
    letra = letra.upper()
    if len(letra) == 1 and letra in alfabeto:
        break
    print("Debe ingresar solo 1 letra")


print("Letra aceptada:", letra)

print(" ".join(oculta))