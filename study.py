from calculation import *
def study(grade):
  choice = input("\nAre you going to study?(Y/N): ")
  if choice == "Y" or choice == "y":
    print("Great!")
    studyChoice(grade)
  elif choice == "N" or choice == "n":
    print("Are you sure? You might forget something.")
    points = -1 #The student will forget something, just because >:]
    final(grade, points)
  else:
    print("Invalid input")
    study(grade)

def studyChoice(grade):
  studyList()
  choice = input()
  points = int(choice)/5
  if points >= 0.5:#3 or more activities
    print("Great job!")
  elif points< 0.5:#less than 3, but more than 0
    print("This is a good start!")
  elif points == 0:#The student said they were going to study, but then not study...
    print("It's not too late to start! Let's try again.")
    studyChoice()#Make them do it again
  final(grade, points)

def studyList():
  print("\nHow many of these activities will you do?:")
  print("* Go over your notes")
  print("* Complete the study guide")
  print("* Read the textbook")
  print("* Go to office hours")
  print("* Go to a study group")
