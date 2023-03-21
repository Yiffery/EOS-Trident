print("Loading calculator:")
print("Importing:         ")
print("  math             ")
import math
print("  os:              ")
print("    system         ")
from os import system
print("Loading functions: ")
print("  clear            ")
def clear():
  system("clear")
clear()
print("Welcome to EOS Calculator")
print("Press r at any time to go back to home")

while True:
  usrinnum1 = input("Enter you first number: ")
  if usrinnum1 == "r":
    clear()
    exec(open("main.py").read())
    usrinop1 = input("Enter your operator *,/,+,-,**,sqrt ")
  if usrinop1 == "r":
    clear()
    exec(open("main.py").read())
    usrinnum2 = input("Enter your second number (not needed for sqrt): ")
    if usrinnum2 == "r":
      clear()
      exec(open("main.py").read())
  
  if usrinop1 == "*":
    print(int(usrinnum1) * int(usrinnum2))
  
  elif usrinop1 == "/":
    print(int(usrinnum1) / int(usrinnum2))
  
  elif usrinop1 == "+":
    print(int(usrinnum1) + int(usrinnum2))
  
  elif usrinop1 == "-":
    print(int(usrinnum1) - int(usrinnum2))
  
  elif usrinop1 == "**":
     print(int(usrinnum1)**int(usrinnum2))
  
  elif usrinop1 == "sqrt":
    print(math.sqrt(int(usrinnum1)))
  
  else:
    print("You didn't enter a valid number and/or an operator.")