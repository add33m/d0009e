# Definiera en funktion för att presentera en meny så jag kan återanvända den för alla uppgifter i labben
def presentMenu(menuItems):
  # Printa alla alternativ
  for i in range(0, len(menuItems)):
    print(str(i + 1) + ":", menuItems[i])
    
  # Kolla om ett av alternativen valts (siffra eller item), och i så fall lämna det, annars hämta ny input
  while True:
    cmd = str(input())
    for i in range(0, len(menuItems)):
      if cmd == str(i+1) or cmd == menuItems[i]:
        return i+1
