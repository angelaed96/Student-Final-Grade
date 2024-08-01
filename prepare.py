from study import study
from calculation import *

def prepare(grade):
  passing = 70 - grade #passing grade is 70%
  if passing > 0:
    print("You need " + str(passing) + "% more in order pass the class with 70%.")
    
  choice = input("\nDid you prepare for the final?(Y/N): ")
  if choice == "Y" or choice == "y":
    print("Great!")
    if grade <= 70:
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
