from typing import Iterable, List, Literal, Union

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
    if alias in self.aliases:
      raise IndexError(f"'{alias}' is already an alias of {self.name}")
    else:
      self.aliases.append(alias)

class Phonebook:
  def __init__(self):
    # Låt people vara en lista med items av klassen Person
    self.people: List[Person] = []

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
        print("Input error:", err)
      except IndexError as err:
        print("Database error:", err)
      except LookupError as err:
        print("File error:", err)
      except SyntaxError as err:
        print(err)

      # Catch-all för resten
      except Exception as err:
        print("An unknown error occurred:", err)

  # Kollar så att rätt mängd argument existerar
  def verifyArgs(self, args: Iterable, amount: int = 2):
    # Kolla så argumenten finns
    if not (args and amount):
      raise ValueError("Missing arguments")

    # Kolla så antalet argument är rätt
    if len(args) != amount:
      raise ValueError(f"Incorrect amount of arguments (expected {amount}, but received {len(args)})")

    for arg in args:
      if not arg:
        raise ValueError("Empty arguments not allowed. Did you use too many spaces?")

  # Söker efter en person med namn/alias
  def get(self, name) -> Union[Person, Literal[False]]:
    # Kolla igenom alla people med __eq__ syntaxen som är definierad för Person-klassen
    for person in self.people:
      if person == name:
        return person
    
    # Om ingen hittas, returna False istället för exception så att funktionen kan användas i ifs utan try-except
    return False

  # Söker efter en person med telefonnummer
  def getFromNum(self, num) -> Union[Person, Literal[False]]:
    # Kolla igenom alla people med __eq__ syntaxen som är definierad för Person-klassen
    for person in self.people:
      if person.num == num:
        return person
    
    # Om ingen hittas, returna False istället för exception så att funktionen kan användas i ifs utan try-except
    return False

  def add(self, args: Iterable):
    self.verifyArgs(args)

    # Kolla så namnet inte är taget
    if self.get(args[0]):
      raise IndexError(f"Person with name or alias {args[0]} already exists. Try adding an alias instead!")

    # Kolla så att numret inte är taget
    personWithNum = self.getFromNum(args[1])
    if personWithNum:
      raise IndexError(f"Phone numbers must be unique ({personWithNum.name} already has number {personWithNum.num})")

    # Skapa en ny person och lägg till den till listan av people
    newPerson = Person(args[0], args[1])
    self.people.append(newPerson)

    return f"Added {args[0]} with phone number {args[1]}"


  def lookup(self, args: Iterable):
    self.verifyArgs(args, 1)
    
    person = self.get(args[0])
    if not person:
      raise IndexError(f"Person with name '{args[0]}' doesn't exist")

    if person.hasAlias(args[0]):
      # Visa ett annat returnvärde om namnet är ett alias
      return f"{args[0]}'s ({person.name}) phone number is {person.num}"
    else:
      return f"{person.name}'s phone number is {person.num}"

  def alias(self, args: Iterable):
    self.verifyArgs(args)

    # Lägg till alias om personen finns, annars raisa error
    person = self.get(args[0])
    if person:
      # Kolla så att personen inte redan har det aliaset
      if person.hasAlias(args[1]):
        raise IndexError(f"'{args[1]}' is already an alias of {person.name}")

      # Dubbelkolla så att aliaset inte redan är taget
      if self.get(args[1]):
        raise ValueError(f"Person with name {args[0]} already exists")

      person.addAlias(args[1])
      return f"Gave {person.name} the alias '{args[1]}'"
    else:
      raise IndexError(f"Person with name '{args[0]}' doesn't exist")

  def change(self, args: Iterable):
    self.verifyArgs(args)

    person = self.get(args[0])
    if not person:
      raise IndexError(f"Person with name '{args[0]}' doesn't exist")

    # Kolla så att numret inte är taget
    personWithNum = self.getFromNum(args[1])
    if personWithNum:
      raise IndexError(f"Phone numbers must be unique ({personWithNum.name} already has number {personWithNum.num})")

    # Förhindra ändringar till samma nummer
    if person.num == args[1]:
      raise ValueError(f"Cannot change to same phone number (number is already {person.num})")

    # Spara det gamla namnet för utskriftens skull
    oldNum = person.num
    person.num = args[1]
    if person.hasAlias(args[0]):
      # Visa ett annat returnvärde om namnet är ett alias
      return f"Changed {args[0]}'s ({person.name}) phone number from {oldNum} to {person.num}"
    else:
      return f"Changed {person.name}'s phone number from {oldNum} to {person.num}"

  def save(self, args: Iterable):
    self.verifyArgs(args, 1)

    # Skapa file handle med with för att slippa behöva stänga den
    with open(args[0], "w") as file:
      for person in self.people:
        # Skapa en lista över all data som ska sparas i raden i rätt ordning, [nummer, namn, alias1, alias2...]
        lineInfo = [person.num, person.name] + person.aliases
        # Sätt ; mellan datan och lägg ;\n på slutet, nummer;namn,alias1,alias2;\n
        lineString = ";".join(lineInfo) + ";\n"
        
        file.write(lineString)
    
    return f"Saved data to '{args[0]}'"

  def load(self, args: Iterable):
    self.verifyArgs(args, 1)

    newData: List[Person] = []
    try:
      # Skapa file handle med with för att slippa behöva stänga den
      with open(args[0], "r") as file:
        # Kom ihåg alla namn och nummer för att förhindra duplicates
        names = []
        nums = []

        # Läs in första raden och fortsätt loopen tills line är en tom rad
        lineNum = 1
        line = file.readline()
        try:
          while line:
            # Dela upp datan genom split och ta bort sista värdet, då det alltid är "\n"
            lineData = line.split(";")
            lineData.pop()

            # Kolla så datan finns/är korrekt formatterad
            if len(lineData) < 2:
              raise ValueError(f"At least 2 values per line are required")

            # Förhindra duplicates
            if lineData[0] in nums:
              raise ValueError(f"Phone numbers must be unique")
            else:
              nums.append(lineData[0])

            if lineData[1] in names:
              raise ValueError(f"Names must be unique")
            else:
              names.append(lineData[1])

            newPerson = Person(lineData[1], lineData[0])
            # Lägg till aliases om de finns
            if len(lineData) > 2:
              for alias in lineData[2:]:
                if alias in names:
                  raise ValueError(f"Aliases must be unique")
                else:
                  names.append(alias)
                  newPerson.addAlias(alias)

            newData.append(newPerson)

            # Läs in nästa rad för att fortsätta loopen
            line = file.readline()
            lineNum += 1
        
        # Hantera fel från när filen lästs in
        except (ValueError, IndexError) as err:
          raise SyntaxError(f"Incorrectly formatted file (on line {lineNum}): {err}")

      # Om datainläsningen lyckades, skriv över datan
      self.people = newData

      return f"Wiped all entries, then loaded data from '{args[0]}'"

    except FileNotFoundError:
      raise LookupError("File not found")


Phonebook().main()
