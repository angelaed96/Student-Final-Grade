from results import results
def final(grade, points):
  #calculating final grade
  total = 200 #Max points on the final
  extra = points * 10 #Points came from studying. Studying will give a max of 10 exrea points
  chance = total * ((grade+extra)/100)
  print("\nOut of 200 points, your final exam score could be " + str(chance))#Esentially, the percentage is based on their academic habits. Their chance is the total of the final times their academic habits.

  final = ((grade*10) + chance)/10 #grade is based on points
  #Dividing by 10 will show percentage
  print ("Your final grade would be " + str(final) + "%\n")

  if final >= 70:
    passed = True
  else:
    passed = False
    
  results(passed)
