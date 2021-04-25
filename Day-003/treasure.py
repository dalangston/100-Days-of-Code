from sys import exit

def print_chest(msg):
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print(f'\n{msg}\n')


if __name__ == '__main__':


    print_chest("Welcome to Treasure Island")


    choice = ''


    print('''
You find yourself on the path at the edge of a dark forrest.  You can go to the
  left or the right.

Which way will you go?

  - left
  - right

''')

    while choice != 'left' and choice != 'right':
        choice = input('> ').lower()

    if choice == 'right':
        print('''
You wander into the dark forest, and losing your way, you fall off a cliff
Your are dead.
''')
        exit()

    print('''
You follow the path until you reach the endge of a lake.  You can wait for the
 boat or you can swim accross the lake.

 What will you do?

  - wait
  - swim

''')

    while choice != 'wait' and choice != 'swim':
        choice = input('> ').lower()

    if choice == 'swim':
        print('''
You enter the cool water and begin to swim.  Suddenly, you feel something brush
 against you leg.  You look back just in time to see the open maw of a giant
 goldfish.
You are dead.
''')
        exit()

    print('''
After an uneventful ride accross the lake you arrive at an enormous castle.
 The castle has three doors, red, blue, yellow. 

 Which door will you choose?

  - red
  - blue
  - yellow

''')

    while choice != 'red' and choice != 'blue' and choice != 'yellow':
        choice = input('> ').lower()

    if choice == 'red':
        print('''
As you enter the room, you knock over the canelabra.  You have only a moment of
 reaization as the room full of straw becomes a raging inferno.
You are dead.
''')
        exit()
    elif choice == 'blue':
        print('''
The door slams behind you.  As you look around the room, the floor begins to fall away
 revealing a pit of lava.  With nowhere to run, and nothing to grab onto, you resign
 yourself to your fate.
You are dead.
''')
        exit()
    else:
        print_chest("Congratulations, you have found the treasure!")
