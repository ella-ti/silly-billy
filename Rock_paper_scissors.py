#🪨Rock, 📄Paper, ✂️Scissors!
import random


print ('===================\n' \
'Rock Paper Scissors\n'
'===================')

name = (input("What's your name? "))


while True:

    cpu = random.choice(['👊', '✋', '✌️'])

    player = int(input('\n''1) 👊\n2) '
                    '✋\n3) ' 
                    '✌️\n '
                    'Pick a number: '))
    
    if player == 1:
        player_choice = '👊'
    elif player == 2:
        player_choice = '✋'
    elif player == 3:
        player_choice = '✌️'
    else:
        print("Invalid choice. Try again!")
        continue

    print(f"{name} chose: {player_choice} ")
    print(f"CPU Chose: {cpu} ")

    if player_choice == cpu:
        print("It's a tie\n")
    elif player_choice == '👊' and cpu == '✌️' or \
        player_choice == '✋' and cpu == '👊' or \
        player_choice == '✌️' and cpu == '✋':
        print(f'{name} wins🎉\n')
    else:
        print(f'{name} loses😔\n')

    again = input('Play again? (Y/N)\n ')
    if again.capitalize() == 'Y':
        continue
    elif again.capitalize() == 'N':
        print("Thank you for playing!")
        break
    
   