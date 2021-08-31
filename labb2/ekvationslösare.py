import math
from typing import Callable

# "Callable[[float], float]" i 1a argumentet innebär att jag kräver en funktion som tar en float och returnerar en float
# Detta gör koden mer type safe, alltså gör det lättare för IDEn att upptäcka misstag på förhand
def derivative(f: Callable[[float], float], x: float, h: float):
  return (f(x+h) - f(x-h)) / (2 * h)

# Testa funktionen med d(sin(pi)), vilket bör vara == -1 (python ger float error dock 😭)
print(derivative(math.sin, math.pi, .0001))

def solve(f: Callable[[float], float], x0: float, h: float):
  # Sätt x i startpositionen
  x = x0
  newX = 0

  # Använder en makeshift do-while loop igen, såklart går det att göra på andra sätt också!
  while True:
    
    # Bara en kopia av den fina matematiska formeln som är inkluderad i labbinstruktionen
    newX = x - f(x) / derivative(f, x, h)

    # Avbryt när rätt noggrannhet uppnåtts
    if abs(x - newX) < h:
      return newX
    else:
      x = newX

# Testa funktionerna
import d0009e_lab2_solveTest
