# Rekursiv bounce
def bounce(n):
  # Skriv "första sidan" av bouncen
  print(n)

  # Om vi är på 0 är vi klara så, annars fortsätt rekursionen
  if (n > 0):
    bounce(n-1)
    # Printa "andra sidan" av bouncen när all undre rekursion är klar
    print(n)

# Behöver math för att floora
import math

# Med rekursion
def tvarsumman(n: int): # tvinga argument n att vara int
  if n < 10:
    return n
  else:
    return (n % 10) + tvarsumman(math.floor(n / 10)) # lämna sista siffran och rekursera med sista siffran borttagen

from typing import Callable

# "Callable[[float], float]" i 1a argumentet innebär att jag kräver en funktion som tar en float och returnerar en float
# Detta gör koden mer type safe, alltså gör det lättare för IDEn att upptäcka misstag på förhand
def derivative(f: Callable[[float], float], x: float, h: float):
  return (f(x+h) - f(x-h)) / (2 * h)

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
