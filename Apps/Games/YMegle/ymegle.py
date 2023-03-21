print("Welome to YMEGLE")
print("The brand new chatting service!")
print("  Version 1.0.0 (Build 2)")
print("Loading Data...")

#IMPORTS
i = 20
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

while i > 5:
  def RELOAD():
  
      
    clear()
    f = open('Apps/Games/YMegle/text.txt', 'r+')
    file_contents = f.read()
    
    clear()
    
    print(file_contents)
    print("\nTIP: Type nothing to reload chat without sending any messages! (UTC Time) Type '/exit' to exit.")
    talk = input("\nTalk : ")
    
    if talk.lower == '/exit':
      clear()
      print('Exiting')
      time.sleep(5)
      exec(open("main.py").read())
    elif talk == '':
      clear()
      
    else:
      print("Sending message...")
      from replit import db as db
       
      f.truncate(0)
      from datetime import datetime, timezone
      from replit import db as db
      now = datetime.now(timezone.utc)
      
      f.write(file_contents + "\n" + str(db["usrcode"]) + " (" + str(now.strftime('%m/%d %H:%M')) + ") "  +": " + talk)
      
      f.close()
      clear()
      print(file_contents)
      
  RELOAD()
print("WHILE TRUE LOOP BROKEN")
time.sleep(5)