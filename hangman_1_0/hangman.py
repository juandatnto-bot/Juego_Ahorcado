"""Archivo principal del juego del ahorcado."""

import random 
from palabras import lista_palabras


palabra_secreta = random.choice(lista_palabras)

oculta = []
for letra in palabra_secreta:
    oculta.append("_")

print(" ".join(oculta))