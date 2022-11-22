print("Loading Dictionary...            ")
print("Importing:                       ")
print("  PyDictionary                   ")
from PyDictionary import PyDictionary
print("Initializing modules:            ")
print("  PyDictionary                   ")
dictionary = PyDictionary()

while True:
        usrdictin = input("Enter a word to find the definition of it (Type 'Exit' to exit app):")
        if usrdictin == "Exit" or "exit":
          exec(open("main.py").read())
        else:
          print(dictionary.meaning(usrdictin))