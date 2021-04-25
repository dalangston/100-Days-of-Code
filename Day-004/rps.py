from random import randint


def print_choices(player, cpu):

    print(f'''
You chose: 
{player}

Your opponent chose:
{cpu}

''')


def play_again(pmt='> '):

    y = ['y',  'yes', 'sure']
    if input(pmt).lower() in y:
        return True

    return False



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choices = [rock, paper, scissors]

again = True
player_won = False

while again:
    choice = -1
    print('''
Choose your option:

 0) Rock
 1) Paper
 2) Scissors

 ''')

    while choice not in [0,1,2]:
        try:
            choice = int(input('> '))
        except:
            print("Selection must be a number")
            continue

        if choice > 2 or choice < 0:
            print("Selection must be one of:  0 1 2")
            continue

    cpu_choice = randint(0,2)

    print_choices(choices[choice], choices[cpu_choice])

    if choice == cpu_choice:
        print('You have tied.\n')

    elif choice == ((cpu_choice + 1) % 3):
        print('You have Won!!\n')

    else:
        print('You have lost\n')

    print("Would you like to play again?")
    again = play_again()

