#The goal of the student is to pass the class with a 70%
#The grade is out of 1,000 points
#The final is 20% of the final grade

from prepare import prepare
from results import results

def goAgain():
  again = input("Want to calculate another grade?(Y/N): ")
  if again == "Y" or again == "y":
    main() #Return to the begining of the program
  elif again == "N" or again == "n":
    print("Good Luck!")
    quit()#exits program
  else:
    print("Invalid input")
    goAgain()
    
def main():
  try:
    percent = float(input("What is your current grade percentage?: "))
  except ValueError:
    print("Invalid input. Please enter a number without the percent sign.")
    main()

  if percent<1 and percent>0:#The student gave a decimal grade
    check = input("Did you mean " + str(percent*100) + "%?(Y/N): ")
    if check == "Y" or check == "y":#Change decimal to percentage
      percent=percent*100
    if check == "N" or check == "n":#Their grade is really that low...
      pass #Do nothing

  grade = percent 
    
  if grade > 100 or grade < 0:
    print("Invalid input. Please enter a grade between 0-100.")
    main()
  elif grade >= 90:
    passed = True
    results(passed) #Even if they don't take the final, they would pass
  else: #89% and under
    prepare(grade)
  goAgain()
  
if __name__ == "__main__":
  main()
  
  

  
  
