'''
Uppgift:

En variant att betala av ett lån är att använda s k rak amortering. Detta innebär att själva skulden betalas av i ett antal
lika stora poster, och att räntekostnaden, som ju beräknas på den kvarvarande skulden, således blir succesivt lägre vid
varje betalning. Den totala kostnaden k för ett lån (dvs all amortering plus total räntekostnad) kan med rak amortering
beräknas med följande formel,
  k = P + (a+1)Pr/2
där P är det lånade beloppet, r är den årliga räntesatsen och a är antal år för återbetalning.

Skriv en funktion kostnad(P, r, a) som beräknar och skriver ut den totala kostnaden för ett lån enligt formeln
ovan. Denna funktion ska sparas i en separat fil (inte samma som uppgift 2). En exempelkörning av funktionen ska kunna se ut så här:
>>> kostnad(50000, 0.03, 10)
Den totala kostnaden efter 10 år är 58250 kr.
'''

def kostnad(P, r, a):
  cost = P + (a+1)*P*r/2
  
  print("Den totala kostnaden efter", a, "år är", cost)
  return cost

kostnad(50000, .03, 10)
