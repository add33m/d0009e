# Importera funktionen jag definierade i menu.py
import menu

# Använder dictionary
def main_dic():
  dic = {} # Skapa dictionary med ordlistan

  while True:
    print("--- Menu for dictionary ---")
    cmd = menu.presentMenu(["Insert", "Lookup", "Exit"])
    
    # WHYYYY kan inte python bara ha en switch case som ett vanligt jävla programmeringsspråk aaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhh
    if cmd == 1:
      key = str(input("Word: "))
      # Förhindra duplicates genom att kolla om ordet redan finns
      if key in dic or key.lower() in dic:
        print("Error: entry already exists for word '" + key + "'")
      # Annars, lägg till ordet
      else:
        val = str(input("Description: "))
        dic[key] = val
        print("Added word", "'" + key + "'", "with discription:", "'" + val + "'")

    elif cmd == 2:
      key = str(input("Word: "))
      # Visa ordets beskrivning om den finns
      if key in dic or key.lower() in dic:
        print("Description for word", "'" + key + "':", dic[key] or dic[str(key).lower()]) # kolla både efter key och key converted till lowercase
      
      # Visa felmeddelande om beskrivning inte finns
      else:
        print("No description found for word '" + key + "'")

    # Avsluta funktionen genom att bryta den oändliga while-loopen
    elif cmd == 3:
      break

# Använder två listor av strängar
# Denna funktion söker inte med lowercase då detta kräver mer jobb med error handling att implementera
def main_dic2():
  # Skapa två listor där ordlistan lagras
  keys = []
  vals = []

  while True:
    print("--- Menu for dictionary ---")
    cmd = menu.presentMenu(["Insert", "Lookup", "Exit"])
    
    # WHYYYY kan inte python bara ha en switch case som ett vanligt jävla programmeringsspråk aaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhh
    if cmd == 1:
      key = str(input("Word: "))
      # Förhindra duplicates genom att kolla om ordet redan finns
      if key in keys:
        print("Error: entry already exists for word '" + key + "'")
      
      # Annars, lägg till ordet
      else:
        val = str(input("Description: "))
        keys.append(key)
        vals.append(val)
        print("Added word", "'" + key + "'", "with discription:", "'" + val + "'")

    elif cmd == 2:
      key = str(input("Word: "))
      # Visa ordets beskrivning om den finns
      if key in keys:
        index = keys.index(key)
        print("Description for word", "'" + key + "':", vals[index])
      
      # Visa felmeddelande om beskrivning inte finns
      else:
        print("No description found for word '" + key + "'")

    # Avsluta funktionen genom att bryta den oändliga while-loopen
    elif cmd == 3:
      break

# Använder en lista av tupler
def main_dic3():
  dic = []

  while True:
    print("--- Menu for dictionary ---")
    cmd = menu.presentMenu(["Insert", "Lookup", "Exit"])
    
    # WHYYYY kan inte python bara ha en switch case som ett vanligt jävla programmeringsspråk aaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhh
    if cmd == 1:
      key = str(input("Word: "))
      # Förhindra duplicates genom att kolla om ordet redan finns
      if list(filter(lambda t: t[0] == key, dic)):
        print("Error: entry already exists for word '" + key + "'")

      # Annars, lägg till ordet
      else:
        val = str(input("Description: "))
        dic.append((key, val))
        print("Added word", "'" + key + "'", "with discription:", "'" + val + "'")

    elif cmd == 2:
      key = str(input("Word: "))
      # Returnerar en array med alla tuples som matchar sökordet
      tuples = list(filter(lambda t: t[0] == key, dic))
      if tuples:
        print("Description for word", "'" + key + "':", tuples[0][1]) # Ta beskrivningen från den första (enda) tuplen som hittats
      
      # Visa felmeddelande om beskrivning inte finns
      else:
        print("No description found for word '" + key + "'")

    # Avsluta funktionen genom att bryta den oändliga while-loopen
    elif cmd == 3:
      break

main_dic3()
