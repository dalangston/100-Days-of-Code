


def print_logo():

    print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")


def get_op():
    
    op = ""

    ops = ['+', '-', '*', '/']

    while not op in ops:

        for i in ops:
            print(i)

        op = input("Choose an operator\n > ")


    return op


def get_operand():


    while True:

        try:
            return float(input("Enter a number\n > "))
        except:
            print("input not a number")


def compute(op1, op2, func):


    if func == "+":
        return op1 + op2
    elif func == "-":
        return op1 - op2
    elif func == "*":
        return op1 * op2
    elif func == "/":
        return op1 / op2
    else:
        print("Unknown function")
        return

def reset_state(full=False):

    if full:
        first = None

    second = None
    result = None
    oper = None


print_logo()

again = True
first = None
second = None
result = None
oper = None

while again:

    if first is None:
        first = get_operand()

    oper = get_op()

    second = get_operand()

    result = compute(first, second, oper)

    print(f"\n{first} {oper} {second} = {result}")

    print("\n\n")

    if input(f"Continue with result {result} ?  (y/n)\n > ").lower() == 'y':
        first = result
        again = True
    elif input("would you like to compute more?  (y/n)\n > ").lower() == 'y':
        first = None
        again = True
    else:
        again = False
