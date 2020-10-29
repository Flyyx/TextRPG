### Formating functions are here

import os, sys
from time import sleep


padding = 55

def debug():
  print("debug")
  input()

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

###――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

def formatContents(lis):
  x = 1
  for i in lis:
    print(color(i.title().ljust(padding,".") + str(x) + "\n"))
    x += 1

###――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

def bPrint(string): ### Ever fifty characters, it line breaks
  ##print(len(string))
  print()
  for i in range(0,len(string),padding):
    ##print("i",i)
    print(string[i:i+padding])
  print()

###――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

def inp(): ### A simplified input function
  return input("Input: ")

###――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

def tryInput(lis): ### Check if the input is valid
  while True:
    x = inp().lower()
    if x in lis:
      return x
    else:
      bPrint("Input invalid, try again.")
      
###――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――  

def screenInitiation(title):
  clear()
  sleep(0.1)
  printBruhBook()
  print((" \033[94m{}\033[0m ".format(title)).center(padding + 10,"―"))
  print()

###――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

def printBruhBook():
  print(color("""  ____             _     ____              _    ___  
 |  _ \           | |   |  _ \            | |  |__ \ 
 | |_) |_ __ _   _| |__ | |_) | ___   ___ | | __  ) |
 |  _ <| '__| | | | '_ \|  _ < / _ \ / _ \| |/ / / / 
 | |_) | |  | |_| | | | | |_) | (_) | (_) |   < / /_ 
 |____/|_|   \__,_|_| |_|____/ \___/ \___/|_|\_\____|
                                                     
                                                     """))

###――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

###――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

def color(string):
  return bcolors.BLUE + string + bcolors.END

###――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

def dog():
  
  print(color("""\n──────▄▀▄─────▄▀▄      ──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄     ─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄ ─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄██▄▄█─█░░▀░░┬░░▀░░█─█▄▄█\n"""))


def cont(): ### Press enter to continue
  bPrint("Press enter to continue.")
  inp()


def loading():
  clear()
  for a in range(0,2):
    for i in range(0,4):
      print("Loading" + "." * i)
      sleep(0.5)
      clear()