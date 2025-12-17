# Write code below 💖

Hufflepuff = 0
Slytherin = 0
Gryffindor = 0
Ravenclaw = 0
print("Answer all questions with the number corresponding with the options")

q1 = int(input('Do you like Dawn or Dusk? \n1) Dawn\n2) Dusk\n3: ' ))
if q1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif q1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print('Wrong input')
  
q2 = int(input('When I’m dead, I want people to remember me as: \n1) The Good \n2) The Great \n3) The Wise \n4) The bold \n5: '))
if q2 == 1:
  Hufflepuff += 2
elif q2 == 2:
  Slytherin += 2
elif q2 == 3:
  Ravenclaw += 2
elif q2 == 4:
  Gryffindor += 2
else:
  print('wrong input')

q3 = int(input('Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum \n5: '))
if q3 == 1:
  Slytherin += 4
elif q3 == 2:
  Hufflepuff += 4
elif q3 == 3:
  Ravenclaw += 4
elif q3 == 4:
  Gryffindor += 4
else:
  print('Wrong input')

highest_score = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

print("Your house with the highest score:")
if Gryffindor == highest_score:
    print("Gryffindor")
if Ravenclaw == highest_score:
    print("Ravenclaw")
if Hufflepuff == highest_score:
    print("Hufflepuff")
if Slytherin == highest_score:
    print("Slytherin")