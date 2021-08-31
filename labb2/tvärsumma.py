# Behöver math för att floora
import math

# Med rekursion
def tvarsumman(n: int): # tvinga argument n att vara int
  if n < 10:
    return n
  else:
    return (n % 10) + tvarsumman(math.floor(n / 10)) # lämna sista siffran och rekursera med sista siffran borttagen

# Med loop
def tvarsumman2(n: int):
  sum = 0
  number = n

  # Python har ingen inbyggd do-while (grumble grumble grumble...)
  while True:
    sum += number % 10

    if number < 10:
      break
    else:
      number = math.floor(number / 10) # ta bort sista siffran om loopen ska fortsätta
  
  return sum

# Testa funktionerna
import d0009e_lab2_sumTest
