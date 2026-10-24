"""Archivo principal del juego del ahorcado."""

import random 
from palabras import lista_palabras
from monigote import etapas


palabra_secreta = random.choice(lista_palabras)

oculta = []
for letra in palabra_secreta:
    oculta.append("_")

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

usadas = [] 

vidas = 6

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
    if vidas == 0:
        print("Has perdido. La palabra era:", palabra_secreta)
        break