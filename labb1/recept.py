'''
Uppgift:

Definiera en funktion recept(antal), som skriver ut en lista på ingredienser till en sockerkaka som är lagom
för det givna antalet personer. Följande recept är lämpligt för 4 personer:
  3 st ägg
  3 dl strösocker
  2 tsk vaniljsocker
  2 tsk bakpulver
  3 dl vetemjöl
  75 g smör
  1 dl vatten

Observera att din funktion måste fungera för godtyckiligt antal personer. 
I utskriften ska antalet ägg vara heltal. 
För väldigt få personer kan det hända att man får 0 ägg. Detta beteende är acceptabelt.

Definiera två olika funktioner för tidsåtgång vid tillagning av sockerkaka:

- En funktion tidblanda(antal) som beräknar och returnerar tiden för att blanda smeten till en sockerkaka för antal personer. 
  Tidsåtgången ska beräknas som 10 minuter fast tid (oavsett antal personer) samt dessutom ytterligare en minut för 
  varje person kakan är avsedd för.

- En funktion tidgradda(antal) som beräknar och returnerar tiden för att grädda kakan, Tidsåtgången ska beräknas som 
  30 minuter fast tid (oavsett antal personer) samt dessutom ytterligare 3 minuter för varje person kakan är avsedd för.

Definiera en funktion sockerkaka(antal) som skriver ut recept för antal personer på skärmen samt tidsåtgång för antal personer. I tidsåtgången ska både tid för gräddning och blandning inkluderas i samma värde (summeras). Funktionerna från (1) och (2) ska användas.
Skriv, i samma fil, ett script (huvudprogram) som skriver ut sockerkaksrecept till 4 och 7 personer på skärmen. Programmet ska alltså skriva ut två recept efter varandra. Här är det noga med att du skriver just ett script, inte en till funktion. Scriptet ska däremot använda din funktion från uppgift 3.

'''

def recept(antal):
  print(round(3 / 4 * antal), "st ägg")
  print(round(3 / 4 * antal, 2), "dl strösocker")
  print(round(2 / 4 * antal, 2), "tsk vaniljsocker")
  print(round(2 / 4 * antal, 2), "tsk bakpulver")
  print(round(3 / 4 * antal, 2), "dl vetemjöl")
  print(round(75 / 4 * antal, 2), "g smör")
  print(round(1 / 4 * antal, 2), "dl vatten")

def tidblanda(antal):
  return 10 + (antal > 0 and antal) or 0

def tidgradda(antal):
  return 3 * tidblanda(antal)

def sockerkaka(antal):
  recept(antal)

  print()
  print("Förberedningstid:", tidblanda(antal))
  print("Gräddtid:", tidgradda(antal))
  print("Total tid:", tidblanda(antal) + tidgradda(antal))

# Printa ut recept för 4 och 7 pers

sockerkaka(4)
print()
sockerkaka(7)
