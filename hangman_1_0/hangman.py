"""Archivo principal del juego del ahorcado."""

import random 
from palabras import lista_palabras


palabra_secreta = random.choice(lista_palabras)

oculta = []
for letra in palabra_secreta:
    oculta.append("_")

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

usadas = []

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
    print("Letra aceptada:", letra)