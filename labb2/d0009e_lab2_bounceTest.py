# -*- coding: latin-1 -*-

from io import StringIO
import sys
#import lab2
#import __main__ as main
import __main__

def testBounce(bounceFkn, printName, num, correctOutput):

  print("Testar "+printName+"("+str(num)+")...",)
  oldStdOut  = sys.stdout
  sys.stdout = StringIO()

  #main.bounce(num)
  bounceFkn(num)

  outString = sys.stdout.getvalue()
  sys.stdout = oldStdOut

  if outString==correctOutput:
    print("funkar!")
  else:
    print("funkar inte!")
    print("Testresultat:")
    print(outString)
    print("Rätt resultat:")
    print(correctOutput)

##def testBounce2():
##  bounceOutput = '0 5 4 3 2 1 0 1 2 3 4 5'
##  oldStdOut  = sys.stdout
##  sys.stdout = StringIO.StringIO()
##
##  try:
##    main.bounce2(0)
##    main.bounce2(5)
##  except AttributeError:
##    sys.stdout = oldStdOut
##    print("Bounce2 finns ej")
##    return
##    
##
##  outString = sys.stdout.getvalue()
##
##  sys.stdout = oldStdOut
##
##  if outString==bounceOutput:
##    print("Bounce2 funkar!")
##  else:
##    print("   Testresultat: ",outString)
##    print("   Rätt resultat: ",bounceOutput)

def suitTestBounce(fkn, printName):
    testBounce(fkn, printName, 5, "5\n4\n3\n2\n1\n0\n1\n2\n3\n4\n5\n")
    testBounce(fkn, printName, 0, "0\n")

#suitTestBounce(__main__.bounce, "bounce")

try:
  suitTestBounce(__main__.bounce, "bounce")
except AttributeError:
  print("'bounce' finns ej.")
try:
  suitTestBounce(__main__.bounce2, "bounce2")
except AttributeError:
  print("'bounce2' finns ej.")
