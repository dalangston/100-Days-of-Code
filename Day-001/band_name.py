print('Welcome to the Band Name Generator.\n')

city = ""
pet = ""

while city == "":
    city = input('What city did you grow up in?\n')

while pet == "":
    pet = input('What is the name of your pet?\n')

print(f'\n Your band name could be:  {city} {pet}')

