from prepare import prepare
from results import results

def again():
  again = input("Want to calculate another grade?(Y/N): ")
  if again == "Y" or again == "y":
    main() #Return to the begining of the program
  elif again == "N" or again == "n":
    print("Good Luck!")
    quit()
    
def main():
  percent = input("What is your current grade percentage?: ")
  grade = float(percent)
  
  if int(grade) >= 90:
    passed = True
    results(passed) #Even if they don't take the final, they would pass
  else: #89% and under
    prepare(grade)
  again()

if __name__ == "__main__":
  main()
  
