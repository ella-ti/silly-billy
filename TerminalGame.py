#Terminal Adventure Game
#Cave
from time import sleep
import random

monsters = random.choices(['Spider', 'Skeleton', 'Zombie'])

hp = 10
mood = 10

escaped = False 

while escaped == False:
    hp = 10
    mood = 10

    story = [
        "\nYour eyes begin to open in what appears to be a dimly lit structure...",
        "You get up and try to look around only to discover...",
        "You are trapped within a prison cell, deep underground.",
        "Around you there is a bed with a blanket, a toilet with a loose handle and a shiny stick.. "
    ]
    for line in story:
        print(line)
        sleep(2)

    c1 = int(input("What item do you choice to try to unlock the cell with?\n1) "
    "The Blanket \n2) "
    "The Toilet Handle \n3) "
    "The Shiny Stick\n "))

    if c1 == 1:
        story = ["\nYou have chosen The Blanket",
            "You try opening the cell door with it..",
            "only dirtying and ripping your blanket apart"]
    
        for line in story:
            print(line)
            sleep(1)
        mood -= 1
        print(f"\nThis action drops your mood.. current mood: {mood}")

    elif c1 == 2:
        story = ["\nYou have chosen The Toilet Handle",
                "You go over to the toilet pulling the handle off..",
                "with this you get a small cut on your hand",
                "you walk over to the cell door and slam it against the lock..",
                "You are succesful in breaking the lock!",
                "The door swings wide open"]
        for line in story:
            print(line)
            sleep(1)
        hp -= 2
        print(f"\nDespite succesfully escaping, you still took damage.. Current hp: {hp}\n")
        escaped = True

    elif c1 == 3:
        story = ["\nYou have chosen The Shiny Stick!",
                 "Upon picking the stick up it snaps in half..",
                 "One half sticks directly into your palm!",
                 "The other piece you inspect and it looks oddly key shaped now..",
                 "You take the key inserting it into the lock",
                 "With a quiet click the door slowly creaks open.."]
        for line in story:
            print(line)
            sleep(2)
            
        hp -= 4
        mood -= 2
        print(f"current stats: {hp}\n{mood}")
        c1_2 = int(input("\nWould you like to take the stick out of your palm?\n1)"
                             "Yes\n2) "
                              "No\n " ))
        if c1_2 == 1:
            story = ["\nYou pull the stick out of your hand..",
            "With an sharp excruciating pain shooting through your hand to the rest of your body ",
            "The pain paralyzes you..",
            "you fall over onto the floor, unable to feel or move anything besides the pain..",
            "you lie there for what feels like forever..",
            "Until your eyes being the close, a bright light is all you can see now..",
            "you enter the peaceful light..",
            "escaping this cell from death."]

            for line in story:
                print(line)
                sleep(2.5)
            hp -= 6
            mood -= 7
            print(f"You final stats are: {hp}\n {mood}")

        elif c1_2 == 2:
            story = ["\nWeighing the pros and cons you decide not to take the shiny stick out of your palm for now..",
            "You look around one last time before leaving the cell.",
            "Glancing at the other objects wondering if they might come in use later..\n"]

            for line in story:
                print(line)
                sleep(2)
        else:
            print("Invalid choice")

        escaped = True

    else:
        print("Invalid choice. Try again.")

#To be continued
        
            



                       
