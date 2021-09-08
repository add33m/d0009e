class Phonebook:
  def __init__(self) -> None:
    self.book = {}
  
  def main(self):
    while True:
      # Vi börjar med att ta ett kommando från användaren
      cmd = str(input("phoneBook> ")).split(" ")  # Ta input och splitta till en lista av delar
      program = cmd[0]                            # Ta ut första ordet som kommandot som ska användas
      args = len(cmd) > 1 and cmd.pop(0) and cmd          # Ta bort första ordet och låt resten vara en lista av argument

      # Inget vanligt kommando kan köras utan argument
      if args:
        # Testa inputten mot alla möjliga kommandon
        if program == "add":
          print(self.add(args))
        elif program == "lookup":
          print(self.lookup(args))
        elif program == "alias":
          print(self.alias(args))

      # Hantera quit
      if program == "quit":
        break

  def add(self, args):
    # Lägg in value arg2 i key arg1 i self.book
    # Orkar inte skapa variabler så detta får vara lite halft oläsbart
    if args[0] and args[1] and not self.book.get(args[0]):
      try:
        # Gör om nummret till en int
        num = int(args[1])
        self.book[args[0]] = num
        return f"Added entry for {args[0]}: {args[1]}"
      except: 
        return ":("
    else:
      return ":("

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
        return "No result..."
    else:
      return ":("

  # Skapa en entry där värdet är en string, så vet performLookup att den ska göra en rekursiv sökning
  def alias(self, args):
    if args[0] and args[1] and self.performLookup(args[0]):
      self.book[args[1]] = args[0]
      return f"Added alias for {args[0]}: {args[1]}"
    else:
      return ":("


Phonebook().main()