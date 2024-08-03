from study import study
from calculation import *

def prepare(grade):
  passing = round(70 - grade) #passing grade is 70%
  if passing > 0:
    print("You need " + str(passing) + "% more in order pass the class with 70%.")
  if grade < 63:
    print("Your only chance to pass is getting a full score on the final and some extra credit.\n Talk to your teacher before it's too late!")
    
  choice = input("\nDid you prepare for the final?(Y/N): ")
  if choice == "Y" or choice == "y":
    print("Great!")
    if grade <= 75:
      print("Let's make sure you're fully prepared.")
      study(grade)
    else:
      print("You should be good to go!")
      points = 3/5
      final(grade, points)
  elif choice == "N" or choice == "n":
    print("We can start now!")
    study(grade)
  else:
    print("Invalid input")
    prepare(grade)
