# Använd den redan definierade menyfunktionen för vi är lata
import menu

# Importera funktionerna från lab2
import lab2

def lab2_menu():
  while True:
    print("--- Menu for lab2 ---")
    cmd = menu.presentMenu(["Bounce", "Tvärsumma", "Newton-Raphson", "Exit"])
    
    # Bounce
    if cmd == 1:
      pos = int(input("Utför bounce från: "))
      print("Executing bounce with:", pos)
      lab2.bounce(pos)

    # Tvärsumma
    elif cmd == 2:
      num = int(input("Beräkna tvärsumma för: "))
      print("Tvärsumman för", num, "är", lab2.tvarsumman(num))

    # Newton-Raphson
    elif cmd == 3:
      num = int(input("Beräkna Newton-Raphson för f(x) = x^2-1 från: "))

      def f(x):
        return x**2 - 1
      
      print("Svar:", lab2.solve(f, num, .0001))

    # Avsluta funktionen genom att bryta den oändliga while-loopen
    elif cmd == 4:
      break

lab2_menu()
