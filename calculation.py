from results import results
def final(grade, points):
  #calculating final grade
  total = 200 #Max points on the final
  extra = points * 15 #Points came from studying. Studying will give a max of 15 extra points
  chance = round(total * ((grade+extra)/100))
  print(extra)
  print(grade)
  print(chance)
  if (chance < 0):#student has a grade of 0 for some reason
    chance = 0
  print("\nOut of 200 points, your final exam score could be " + str(chance))#Esentially, the percentage is based on their academic habits. Their chance is the total of the final times their academic habits.

  final = ((grade*8) + chance)/10 #grade is based on points
  #Dividing by 10 will show percentage
  print ("Your final grade would be " + str(final) + "%\n")

  if final >= 70:
    passed = True
  else:
    passed = False
    
  results(passed)
