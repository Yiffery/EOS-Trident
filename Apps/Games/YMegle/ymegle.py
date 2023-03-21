print("Welome to YMEGLE")
print("The brand new chatting service!")
print("  Version 1.0.0 (Build 2)")
print("Loading Data...")

#IMPORTS

from os import system
from datetime import datetime, timezone
from replit import db as db
import time
import random

db["usrcode"] = 0000

def clear():
  system('clear')

clear()

db["usrcode"] = random.randint(0000,9999)
print("Your username is: " + str(db["usrcode"]))
time.sleep(2)

while True:
  def LOAD():
    
    clear()
    f = open('Apps/Games/YMegle/text.txt', 'r+')
    file_contents = f.read()
    
    clear()
    
    print(file_contents)
    print("\nTIP: Type nothing to reload chat without sending any messages! (UTC Time) Type '/exit' to exit.")
    talk = input("\nTalk : ")
    
    if talk == '':
      print("CONTINUE")
    elif talk != '/exit' or '/Exit':
      clear()
      exec(open("main.py").read())
    else:
      print("Sending message...")
      from datetime import datetime, timezone
      from replit import db as db
       
      f.truncate(0)
      now = datetime.now(timezone.utc)
      
      f.write(file_contents + "\n" + str(db["usrcode"]) + " (" + str(now.strftime('%m/%d %H:%M')) + ") "  +": " + talk)
      
      f.close()
      clear()
      print(file_contents)
    
  LOAD()