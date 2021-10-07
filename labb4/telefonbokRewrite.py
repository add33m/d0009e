from typing import Iterable, Literal, Union

"""
  Detta är en rewrite av telefonbok.py som dels följer reglerna i labben (den första använde ints för
  att lagra telefonnummer, vilket inte är tillåtet) och dels har mycket snyggare felhantering genom
  pythons exception-system
"""

class Person:
  def __init__(self, name: str, number: str):
    self.name = name
    self.num = number
    self.aliases = []

  # True om det jämförda namnet är personens namn eller ett av personens alias (namnet finns i aliases)
  def __eq__(self, name: str) -> bool:
    return self.name == name or name in self.aliases

  # Kollar om namnet är ett alias för personen
  def hasAlias(self, alias: str):
    return alias in self.aliases

  # Lägger till ett alias
  def addAlias(self, alias: str):
    self.aliases.append(alias)

class Phonebook:
  def __init__(self):
    # Låt people vara en lista med items av klassen Person
    self.people = []

  def main(self):
    while True:
      # Vi börjar med att ta ett kommando från användaren
      cmd = str(input("Phonebook> ")).split(" ")  # Ta input och splitta till en lista av delar
      program = cmd[0].lower()                    # Ta ut första ordet som kommandot som ska användas
      args = len(cmd) > 1 and cmd.pop(0) and cmd  # Ta bort första ordet och låt resten vara en lista av argument

      # Hantera quit
      if program == "quit":
        break

      try:
        # Inget vanligt kommando kan köras utan argument
        # if not args:
        #   raise ValueError("Missing arguments")

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
      except IndexError as err:
        print("Error:", err)

  # Kollar så att rätt mängd argument existerar
  def verifyArgs(self, args: Iterable, amount: int = 2):
    # Kolla så argumenten finns
    if args and amount:

      # Kolla så antalet argument är rätt
      if len(args) == amount:
        return True
      else:
        raise ValueError(f"Incorrect amount of arguments (expected {amount}, but received {len(args)})")

    else:
      raise ValueError("Missing arguments")

  def get(self, name) -> Union[Person, Literal[False]]:
    # Kolla igenom alla people med __eq__ syntaxen som är definierad för Person-klassen
    for person in self.people:
      if person == name:
        return person
    
    # Om ingen hittas, returna False istället för exception så att funktionen kan användas i ifs utan try-except
    return False

  def add(self, args: Iterable):
    self.verifyArgs(args)

    # Kolla duplicates
    if not self.get(args[0]):
      # Skapa en ny person och lägg till den till listan av people
      newPerson = Person(args[0], args[1])
      self.people.append(newPerson)

      return f"Added {args[0]} with phone number {args[1]}"

    else:
      # Hantera duplicate
      raise IndexError(f"Person with name {args[0]} already exists. Try adding an alias instead!")

  def lookup(self, args: Iterable):
    self.verifyArgs(args, 1)
    
    person = self.get(args[0])
    if person:
      if person.hasAlias(args[0]):
        # Visa ett annat returnvärde om namnet är ett alias
        return f"{args[0]}'s ({person.name}) phone number is {person.num}"
      else:
        return f"{person.name}'s phone number is {person.num}"
    else:
      raise IndexError(f"Person with name '{args[0]}' doesn't exist")

  def alias(self, args: Iterable):
    self.verifyArgs(args)

    # Lägg till alias om personen finns, annars raisa error
    person = self.get(args[0])
    if person:
      person.addAlias(args[1])
      return f"Gave {person.name} the alias '{args[1]}'"
    else:
      raise IndexError(f"Person with name '{args[0]}' doesn't exist")
      

Phonebook().main()
