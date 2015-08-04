import random
import csv
import string
import re

class Movie(object):
 movie = ""
 def __init__(self):
  self.getmovie()
  return
  
 def csvtoarray(self): 
  fileinput = "C:\Users\PV02594\Desktop\input.csv"
  csvfile = open(fileinput, 'rb')
  for line in csvfile:
   l = [i.strip() for i in line.split(',')]
  return l
 
 def randommovie(self, l): 
  movie = random.sample(l, 1)
  return ''.join(movie)

 def getmovie(self): 
  l = self.csvtoarray()
  self.movie = self.randommovie(l)
  return

class HangMan(Movie):
 #global variables
 count = 7
 win = 0
 original = []
 temp = []
 def __init__(self):
  self.startPlay()
  return

 def startPlay(self):
  print ("Welcome to HangMan!!!")
  start = raw_input("Press 1 to start the game...\n")
  if int(start) == 1:
   print ("Let's start the game.... \nGuess the movie:\n")
   super(HangMan, self).__init__()
   print "\t\t\t",self.playWindow()
   while self.count > 0:
    self.startGuessing()
    if self.temp == self.original:
	  print "\nCongratulations!!! You have cracked the movie"
	  self.win = 1
	  break
    print  "\nGuesses left: ", self.count
   if self.win != 1:
    print "\nOops!!! You have no chances left....Better Luck next time\n The Movie name is", ''.join(self.original)
  else:
   print "Wrong selection....Try again"
   return
  return  
  
 def playWindow(self):
  self.original = list(self.movie)
  self.temp = list(self.movie)
 
  for index, item in enumerate(self.temp):
    if item != ' ':
        self.temp[index] = '_'
 
  return ' '.join(self.temp)
 
 def startGuessing(self): 
  letter = re.compile(r'[a-zA-Z0-9]+') #This will check for alphabet.
  input = raw_input("\nGuess a letter:\n\n") #ask the user for input.
  input = self.validateInput(input, letter)
  self.UpdateLetters(input)
  #print self.temp
  return
  
  
 def validateInput(self, input, letter):
  while not letter.match(input) : 
    print "invalid characters"
    input = raw_input("\nGuess a letter:\n\n")
  return input
  
 def UpdateLetters(self, input):  
  indexes = [ i for i, word in enumerate(self.original) if word.lower() == str(input).lower() ] # gives index where the character matches
  if(len(indexes) == 0):
   self.count -= 1
  else:
   for j in indexes:
	 self.temp[j] = self.original[j]
  print "\t\t\t",' '.join(self.temp)
  return
   
h = HangMan()  #main call
  
  

 


