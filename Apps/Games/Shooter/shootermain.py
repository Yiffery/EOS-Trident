print("Loading Shooter...  ")
print("Importing:          ")
print("  time              ")
import time
print("  random            ")
import random
print("  os:               ")
print("    system          ")
from os import system
print("Loading functions:  ")
print("  clear             ")
def clear():
  system("clear")
print("Loading variables   ")
print("  pcchoicelist      ")
pcchoicelist = ["Shoot", "Block", "Reload"]
print("  ammo              ")
ammo = 1

clear()

while True:
  #Ask the user shoot/block/reload
  print("Ammo:")
  print(ammo)
  usrchoice = input("Shoot/Block/Reload: ").lower()
  #Determine what the computer choses and print it
  pcchoice = random.choice(pcchoicelist).lower()
  print("The computer chose " + pcchoice)

  #Ties
  if usrchoice == "shoot" and pcchoice == "shoot":
    if ammo < 1:
      print("You don't have any ammo.")
    elif ammo > 1:
      ammo = ammo - 1
      time.sleep(1)
      print("Tie!")

  elif usrchoice == "shoot" and pcchoice == "block":
    if ammo < 1:
      print("You don't have any ammo.")
    elif ammo > 1:
      ammo = ammo - 1
      time.sleep(1)
      print("Tie!")

  elif usrchoice == "block" and pcchoice == "shoot":
    time.sleep(1)
    print("Tie!")

  elif usrchoice == "block" and pcchoice == "shoot":
    time.sleep(1)
    print("Tie!")

  elif usrchoice == "reload" and pcchoice == "reload":
    ammo = ammo + 1
    time.sleep(1)
    print("Tie!")

  #PC wins
  elif usrchoice == "reload" and pcchoice == "shoot":
    ammo = ammo + 1
    time.sleep(1)
    print("You lost!")
    ammo = 1
    time.sleep(1)
    usrask = input("Return to home? y/n ").lower()
    if usrask == "y":
      exec(open("main.py").read())

  #Computer wins
  elif usrchoice == "shoot" and pcchoice == "reload":
    if ammo < 1:
      print("You don't have any ammo.")
    elif ammo > 1:
      ammo = ammo - 1
      time.sleep(1)
      print("You win!")
      ammo = 1
      time.sleep(1)
      usrask = input("Return to home? y/n ").lower()
      if usrask == "y":
        exec(open("main.py").read())