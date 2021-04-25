


def print_logo():

    print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")


def get_message():
    """ Get message to encrypt or decrypt """

    message = ""

    while message == "":
        message = input("Enter the message\n > ")

    return message


def get_shift():
    """ Get shift value for ceaser cipher """

    shift = 0
    while not shift > 0:
        try:
            shift = int(input("What is the shift number?\n > "))
        except:
            print("Shift Number must be a number greater than 0\n")

    return shift


def get_mode():
    """ Select Encrypt or Decrypt """


    mode = 0
    print("""
Would you like to encrypt or decrypt:

 1 - Encrypt
 2 - Decrypt

 """)

    while not mode in [1, 2]:
        try:
            mode = int(input(" > "))
        except:
            print("\nSelect 1 or 2\n)")

    return mode

def do_again():
    """ Would you like to play again? """

    print("Would you like to do another? (y or n)")
    while True:
        ans = input(" > ")
        if ans.lower() == 'y':
            return True

        return False
        


def run_cipher(message, shift):
    """ Run ceaser cipher on message with specified alphabet shift """

    last = len(message) - 1
    new_msg = ""

    abet = alphabet

    for c in [x for x in message]:
        old_pos = abet.index(c)
        new_pos = (old_pos + shift) % len(abet)

        new_msg += abet[new_pos]

    return new_msg



def gen_alphabet():
    """ Generate Alphabet to use for ceaser cipher """
    alphabet = (
            [chr(x) for x in range(97,123)] + [chr(x) for x in range(65, 91)] +
            [chr(x) for x in range(48, 58)] + [chr(x) for x in range(20, 48)] +
            [chr(x) for x in range(58, 65)] + [chr(x) for x in range(91, 97)] +
            [chr(x) for x in range(123, 127)]
            )

    return alphabet


if __name__ ==  '__main__':


    print_logo()

    again = True

    alphabet = gen_alphabet()

    while again:

        if get_mode() == 1:
            decrypt = False
        else:
            decrypt = True

        msg = get_message()

        shift = get_shift()

        if decrypt:
            shift *= -1
        
        print(f"Here is your result\n {run_cipher(msg, shift)}")

        again = do_again()

