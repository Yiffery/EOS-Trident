print("--------        -----           -----     ")
print("|             /       \        /          ")
print("|            /         \      |           ")
print("|           |           |      \          ")
print("--------    |           |       -----     ")
print("|           |           |            \    ")
print("|            \         /              |   ")
print("|             \       /              /    ")
print("--------        -----           -----     ")
print("                                          ")
print("Importing modules:                        ")
print("  time                                    ")
import time
print("  os:                                     ")
print("    system                                ")
from os import system
print("Loading variables:                        ")
print("  usrinapp                                ")
usrinapp = 0
print("Loading functions:                        ")
print("  clear                                   ")
def clear():
  system('clear')

clear()
def main():
  clear()
  #Home screen
  print("EOS 0.5.8")
  print("Build 1")
  print()
  print("-------------------------- ")
  print("Applications:              ")
  print("  >Games:                  ")
  print("    1.0 - Shooter          ")
  print("    1.1 - YMegle           ")
  print("  >Utilities:              ")
  print("    2.0 - Calculator       ")
  print("    2.1 - Dictionary       ")
  print("    2.2 - Power options    ")
  print("                           ")
  print("  4 - Credits              ")
  print("-------------------------- ")
  print()
  #Ask the user to input a number
  print("Input a number corresponding to the            ")
  usrinapp = input("application you would like to run:  ")
  
  #Launch apps
  if usrinapp == "turtleUI":
    usrinapp = 0
    clear()
    exec(open("turtleUI.py").read())
  #1.0 - Shooter
  if usrinapp == "1.0":
    #Reset usrinapp and clear the screen
    usrinapp = 0
    clear()
    exec(open("Apps/Games/Shooter/shootermain.py").read())
    
  #1.1 - YMegle
  if usrinapp == "1.1":
    #Reset usrinapp and clear the screen
    usrinapp = 0
    clear()
    exec(open("Apps/Games/YMegle/ymegle.py").read())
    
  #2.0 - Calculator
  if usrinapp == "2.0":
    #Reset usrinapp and clear the screen
    usrinapp = 0
    clear()
    exec(open("Apps/Utilities/Calculator/calcmain.py").read())
  
  #2.1 - Dictionary
  if usrinapp == "2.1":
    #Reset usrinapp and clear the screen
    usrinapp = 0
    clear()
    exec(open("Apps/Utilities/Dictionary/dictmain.py").read())

  #2.2 - Power options (Shutdown/Restart)
  if usrinapp == "2.2":
    #Reset usrinapp and clear the screen
    usrinapp = 0
    clear()
    exec(open("Apps/Utilities/Power_options/pwoptmain.py").read())

  #4 - Credits
  if usrinapp == "4":
    #Reset usrinapp and clear the screen
    usrinapp = 0
    clear()
    exec(open("Apps/Utilities/Credits/creditmain.py").read())

  else:
    clear()
    print("That was not a valid option.")
    time.sleep(1.5)
    clear()
    main()
    
main()