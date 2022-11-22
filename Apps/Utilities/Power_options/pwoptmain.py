print("Loading Power Options...    ")
print("Importing:                  ")
print("  time                      ")
import time
print("  os:                       ")
print("    system                  ")
from os import system
print("Loading functions:          ")
print("  clear                     ")
def clear():
  system("clear")

def shutdownoptions():
  print("-------------------------- ")
  print("Shutdown Options:")
  print("  1 - Shutdown")
  print("  2 - Restart")
  print("-------------------------- ")
  print("")
  pwinop = input("Please enter your option: ")
  
  if pwinop == "1":
    print("Shutting down...")
    time.sleep(2)
    clear()
      
  elif pwinop == "2":
    print("Restarting...")
    time.sleep(2)
    clear()
    exec(open("main.py").read())
  else:
    clear()
    print("That was not a option.")
    time.sleep(2)
    shutdownoptions()
shutdownoptions()