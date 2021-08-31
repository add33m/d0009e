# Rekursiv bounce
def bounce(n):
  # Skriv "första sidan" av bouncen
  print(n)

  # Om vi är på 0 är vi klara så, annars fortsätt rekursionen
  if (n > 0):
    bounce(n-1)
    # Printa "andra sidan" av bouncen när all undre rekursion är klar
    print(n)

# Loop-baserad bounce (jag använder for-loop, men man kan också använda while)
def bounce2(n):
  # Gå från -n till n (stannar på n+1, så n blir sista som printas)
  for i in range(-n, n+1):
    print(abs(i)) # printa absolutvärdet av i så det alltid är positivt

# Testa funktionerna
import d0009e_lab2_bounceTest
