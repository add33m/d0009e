# -*- coding: latin-1 -*-

#import StringIO
import sys
#import lab2
import __main__ as main

def testfun1(x):
  return x**2-1

def testSolve(solvF, start, solution, precision):

  print("Testar solve för f(x)=x^2-1 med startpunkt x="+str(start)+"...")

  xs=solvF(testfun1, start, precision)

  if solution-precision <= xs <= solution+precision:
    print("funkar!")
  else:
    print("funkar inte!")
    print("   Testresultat:  ",xs)
    print("   Rätt resultat: ",solution,"+-",precision)

testSolve(main.solve, 10, 1, 0.1)
testSolve(main.solve, -10, -1, 0.1)
