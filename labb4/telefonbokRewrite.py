from typing import List


class Person:
  def __init__(self, name: str, number: str):
    self.name = name
    self.num = number
    self.aliases = []

  # Returns true if name is an alias or true name of person
  def __eq__(self, name: str) -> bool:
    return self.name == name or name in self.aliases  

class Phonebook:
  def __init__(self):
    # Låt people vara en lista med items av klassen Person
    self.people = []

  def main(self):
    while True:
      # Vi börjar med att ta ett kommando från användaren
      cmd = str(input("phoneBook> ")).split(" ")  # Ta input och splitta till en lista av delar
      program = cmd[0]                            # Ta ut första ordet som kommandot som ska användas
      args = len(cmd) > 1 and cmd.pop(0) and cmd          # Ta bort första ordet och låt resten vara en lista av argument

      # Hantera quit
      if program == "quit":
        break

      try:
        # Inget vanligt kommando kan köras utan argument
        if not args:
          raise ValueError("Missing arguments")

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
          raise ValueError("Invalid command")

      except ValueError as err:
        print("Error:", err)

  def get(self, name):
    # Look through all saved people using the __eq__ syntax defined for the person class
    for person in self.people:
      if person == name:
        return person
    
    # If noone is found, raise error
    raise IndexError("Person with that name not found")

  def add(args):
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

pb = Phonebook()
pb.main()

pb2 = Phonebook()
pb2.main()