from random import randint
from random import choice as rc
from random import shuffle

pw_len = 0
special_cnt = 0
num_cnt = 0


letters = [chr(c) for c in range(65, 91)] + [chr(c) for c in range(97, 123)]
numbers = [chr(c) for c in range(48, 58)]
special = (
        [chr(c) for c in range(33, 48)] + [chr(c) for c in range(58, 65)] +
        [chr(c) for c in range(92, 97)] + [chr(c) for c in range(122, 127)]
            )

while True:
    while pw_len < 8:
        try:
            pw_len = int(input("How many characters would you like in the Password? (min length = 8)\n  > "))
        except:
            print("Length must be a number")

    while special_cnt < 2:
        try:
            special_cnt = int(input("How many special characters would you like? (min = 2)\n  > "))
        except:
            print("Must be a number")

    while num_cnt < 2:
        try:
            num_cnt = int(input("How many numbers would you like in the Password? (min = 2)\n  > "))
        except:
            print("Must be a number")

    if pw_len - special_cnt - num_cnt >= 0:
        break

    print("\nCharacter count conflict\n\n")
    pw_len = 0
    special_cnt = 0
    num_cnt = 0

pw_chars = (
        [rc(numbers) for x in range(num_cnt)] +
        [rc(special) for x in range(special_cnt)] +
        [rc(letters) for x in range(pw_len - special_cnt - num_cnt)]
        )

pw = ''

for i in range(pw_len):
    pw += pw_chars.pop(randint(0, len(pw_chars)-1))

print(f'Your password is:\n  {pw}')
