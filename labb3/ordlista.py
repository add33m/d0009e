# Importera funktionen jag definierade i menu.py
import menu

def main_dic():
  dic = {} # Skapa dictionary med ordlistan

  while True:
    print("--- Menu for dictionary ---")
    cmd = menu.presentMenu(["Insert", "Lookup", "Exit"])
    
    # WHYYYY kan inte python bara ha en switch case som ett vanligt jävla programmeringsspråk aaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhh
    if cmd == 1:
      key = str(input("Word: "))
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

main_dic()
