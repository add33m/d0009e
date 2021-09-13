class Phonebook:
  def __init__(self) -> None:
    self.book = {}
  
  def main(self):
    while True:
      # Vi börjar med att ta ett kommando från användaren
      cmd = str(input("phoneBook> ")).split(" ")  # Ta input och splitta till en lista av delar
      program = cmd[0]                            # Ta ut första ordet som kommandot som ska användas
      args = len(cmd) > 1 and cmd.pop(0) and cmd          # Ta bort första ordet och låt resten vara en lista av argument

      # Hantera quit
      if program == "quit":
        break

      # Inget vanligt kommando kan köras utan argument
      if args:
        # Testa inputten mot alla möjliga kommandon
        if program == "add":
          print(self.add(args))
        elif program == "lookup":
          print(self.lookup(args))
        elif program == "alias":
          print(self.alias(args))
        elif program == "change":
          print(self.change(args))
        elif program == "save":
          print(self.save(args))
        elif program == "load":
          print(self.load(args))
        
        # Om kommandot inte finns
        else:
          print("Invalid command")

      # Om inga argument finns
      else:
        print("Missing argument(s)")


  def add(self, args):
    # Lägg in value arg2 i key arg1 i self.book
    # Orkar inte skapa variabler så detta får vara lite halft oläsbart
    if args[0] and args[1] and not self.book.get(args[0]):
      try:
        # Gör om numret till en int
        num = int(args[1])
        self.book[args[0]] = num
        return f"Added entry for {args[0]}: {args[1]}"
      except: 
        return f"{args[1]} is not a valid number"
    else:
      return args[0] and args[1] and f"Entry already exists for {args[0]}" or "Invalid or missing argument(s)"

  # Funktion som rekursivt kan söka genom aliases och returna svaret istället för en string
  def performLookup(self, search):
    if search:
      result = self.book.get(search)
      if result:
        # Om resultatet är en sträng, genomför en ny sökning med resultatet som sträng, annars returna resultatet
        return type(result) == str and self.performLookup(result) or result

      # Hantera avsaknat resultat
      else:
        return None

    # Hantera ogiltig söksträng
    else:
      return None

  # Funktion som använder performLookup för att svara med en sträng som kan printas
  def lookup(self, args):
    if args[0]:
      result = self.performLookup(args[0])
      if result:
        return f"Entry found for {args[0]}: {result}"
      else:
        return f"No entry found for {args[0]}"
    else:
      return "Invalid or missing argument"

  # Skapa en entry där värdet är en string, så vet performLookup att den ska göra en rekursiv sökning
  def alias(self, args):
    if args[0] and args[1] and self.performLookup(args[0]):
      self.book[args[1]] = args[0]
      return f"Added alias for {args[0]}: {args[1]}"
    else:
      return args[0] and args[1] and f"No entry exists for {args[0]}" or "Invalid or missing argument(s)"
  
  # Fungerar på samma sätt som performLookup fast ändrar värdet istället för att returna det
  def performChange(self, search, newVal):
    if search:
      result = self.book.get(search)
      if result:
        # Om resultatet är en sträng, genomför en ny sökning med resultatet som sträng, annars ändra värdet
        if type(result) == str:
          self.performChange(result, newVal)
        else:
          try:
            # Gör om numret till en int
            num = int(newVal)
            self.book[search] = num
          except:
            return None
        
        return "Success"

      # Hantera avsaknat resultat
      else:
        return None

    # Hantera ogiltig söksträng
    else:
      return None

  # Om det finns ett nummer för namnet, ändra det till det nya
  def change(self, args):
    # Dubbelkolla att argumenten och värdet finns
    if args[0] and args[1] and self.performLookup(args[0]):
      
      # Försök ändra värdet och kolla hur det gick
      if self.performChange(args[0], args[1]):
        return f"Changed number for {args[0]}: {args[1]}"
      else:
        return f"Failed to change number for {args[0]}"

    else:
      return args[0] and args[1] and f"No entry exists for {args[0]}" or "Invalid or missing argument(s)"

  # Spara den nuvarande tabellen/telefonboken till fil
  def save(self, args):
    # Kolla så att arg0 (filnamn) finns
    if args[0]:
      # Skapa en sträng som går att spara till filen som angetts
      result = ""

      # Lägg till varje värde i tabellen
      for key in self.book:
        val = self.performLookup(key)
        result += f"{key};{val};\n" # Lägg till en ny rad med format: key;value;

      # Spara till filen
      try:
        with open(args[0], "w") as file:
          file.write(result)
          return f"Successfully saved data to {args[0]}"
      except:
        return f"Failed to save data to {args[0]}"
    
    # Något gick fel
    return "Invalid or missing argument"

  # Ladda en tabell/telefonbok från fil
  def load(self, args):
    # Kolla så att arg0 (filnamn) finns
    if args[0]:
      # Ladda filen
      try:
        with open(args[0], "r") as file:
          saveData = file.read()
          if saveData:
            # Gå igenom och splitta upp strängen efter först \n, sedan ;
            self.book = {} # Skapa en ny tabell
            lines = saveData.split("\n")
            for line in lines:
              lineData = line.split(";")
              # Skriv sedan in det i den nya tabellen
              if lineData[0] and lineData[1]:
                self.book[lineData[0]] = int(lineData[1])
            
            return f"Successfully loaded data from {args[0]}, {lines} entries found"
      
          # saveData finns inte eller är tom
          else:
            return "Missing save data"
      except:
        return f"Failed to load file {args[0]}"

    # Något gick fel
    return "Invalid or missing argument"


Phonebook().main()