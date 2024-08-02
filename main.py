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
  percent = input("What is your current grade percentage?: ")
  if not percent.isnumeric():
    print("Invalid input. Please enter a whole number without the percent sign.")
    main()
  else:
    grade = float(percent)
    
  if int(grade)>100 or int(grade)<0:
    print("Invalid input. Please enter a grade between 0-100.")
    main()
  elif int(grade) >= 90:
    passed = True
    results(passed) #Even if they don't take the final, they would pass
  else: #89% and under
    prepare(grade)
  goAgain()
  
if __name__ == "__main__":
  main()
  
  
