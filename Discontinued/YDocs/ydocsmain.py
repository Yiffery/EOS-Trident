#Import
from replit import db
from os import system
import time

#Varibles
alldocumentnames = db.prefix("name")
alldocumenttext = db.prefix("text")
documentnumberformainscreen = 0
documentnumberforselector = 0
documentnumberforopener = 0
opneneddocumentnumber = 0

#Definitions
def clear():
  system('clear')


clear()
print("Welcome to YDocs")
print()

for z in alldocumentnames:
    print("yas")
    documentnumberforselector += 1
for x in alldocumentnames:
  documentnumberformainscreen += 1
  print("  " + str(documentnumberformainscreen) + " - " + db[x])
print("")
input1 = input(
  "Enter Document Number Here (Type 'New' to Create New Document): ").lower()


if str(input1) != "new":
  print('checkpoint1')
  time.sleep(5)
  
  for z in alldocumentnames:
    print("yas")
    documentnumberforselector += 1
      
    if documentnumberforselector == str(input1):
      print("passed 2")
      time.sleep(5)
      for y in alldocumentnames:
        documentnumberforopener += 1
        if documentnumberforopener == str(input1):
          clear()
          
          print("DEV:"+documentnumberforselector)
          print("DEV:"+documentnumberforopener)
          print("DEV:")
          time.sleep(1)
          opneneddocumentnumber = documentnumberforopener
          print("YDocs")
          print("Document Title: " + y)
          documentname = input("Change Document Name: ")

          db["name" + opneneddocumentnumber] = documentname
          clear()
          print("YDocs")
          print("Document Contents:")
          opendocumentcontents = db["text" + documentnumberforopener]
          print(opendocumentcontents)
          doccontents = input(">>> ")
          db["text" + opneneddocumentnumber] = doccontents
          clear()
          print("Document Saved")
          time.sleep(1.5)
          clear()
          print("Returning to Home...")
          time.sleep(3)
          clear()
          exec(open("main.py").read())
else:
  print("You didn't enter anything the OS could recognize")

if str(input1) == "New" or "new":
  print("DEV: Creating new doc?")
  for y in alldocumentnames:
    documentnumberforopener += 1
  opendocumentnumber = documentnumberforopener + 1
  clear()
  print("Enter New Document Name")
  docname = input(">>> ")
  db["name" + str(opendocumentnumber)] = docname
  clear()
  print("Enter New Document Contents")
  doccontents = input(">>> ")
  clear()
  print("Saving...")
  db["text"+str(opendocumentnumber)] = doccontents
  print("Saved.")
  time.sleep(1)
  exec(open("main.py").read())
  
else:
  print("That was not an option.")
