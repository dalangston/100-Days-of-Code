print("Welcome to the Tip Calculator\n")

total = 0
ways_split = 1
percent = 0

while not total > 0:
    total = float(input("What was the bill total?\n"))

ways_split = int(input("How many people will split the bill?\n"))

if ways_split < 1:
    ways_spllit = 1

percent = float(input("What percentage tip woule you like to give?\n"))

print(f"Each person should pay: ${(total * (1 + (percent/100))) / ways_split:.2f}")
