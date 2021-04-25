import os

def print_logo():

    print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
                              ''')


def clear_screen():
    

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def get_bid():

    bidder = input("Waht is your name? ")
    bid = float(input("What is your bid?  $"))

    bids[bidder] = bid


def get_high_bid(bids):


    high_bid = 0
    winner = ''


    for bidder in bids:
        if bids[bidder] > high_bid:
            winner = bidder
            high_bid = bids[bidder]

    return winner

    #return max(bids, key=bids.get)


more = 'y'
bids = {}


while more == 'y':

    more = ''
    print_logo()


    get_bid()

    while not more in ['y', 'n']:
        more = input("Is there another bidder? (y/n)\n > ").lower()

    clear_screen()


winner = get_high_bid(bids)

print(f"\n\nThe winner is {winner}\nWinning bid:  ${bids[winner]:.2f}")
