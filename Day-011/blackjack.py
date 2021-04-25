from random import shuffle
from sys import exit
import os


def clear_screen():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_logo():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")


def gen_deck(num_decks=1):
    """Generate new deck(s)"""

    deck_size = 52 * num_decks

    deck = [x for x in range(deck_size)]
    shuffle(deck)

    return deck


def score_hand(cards):
    """Score cards in the hand"""

    score = 0

    aces = 0
     
    for card in cards:
        if card % 13 == 0:
            score += 11
            aces += 1
        elif card % 13 >= 10:
            score += 10
        else:
            score += (card % 13) + 1
    
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def decode_card(card):
    """Get the card maped to its ordinal position"""

    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    #return f"{cards[card % 13]}({card % 13})"
    return f"{cards[card % 13]}"


def deal_cards(num_cards):

    global deck

    cards = []

    for card in range(num_cards):
        try:
            cards.append(deck.pop())
        except:
            deck = gen_deck()

    return cards


def turn_loop(p_hand, d_hand):
    """Main loop of player's turn"""

    player_score = score_hand(p_hand)
    dealer_score = score_hand(d_hand[:1])

    while player_score <= 21:

        print(f"""
Choose your action:

Dealer Hand:  ({dealer_score} ?)
              {decode_card(d_hand[0])} ?


Your Hand:    ({player_score})
              {'  '.join([decode_card(x) for x in p_hand])}



(H)it
(S)tand

""")
        player_action = input(" > ").lower()

        if player_action == "h":
            p_hand.extend(deal_cards(1))
            player_score = score_hand(p_hand)
            clear_screen()
        elif player_action == "s":
            return p_hand
        else:
            continue

        if player_score > 21:
            print("BUST")
            end_game(False, p_hand, d_hand)

    return p_hand


def dealer_loop(d_hand, p_hand):
    """Main loop of dealer's turn"""

    dealer_score = score_hand(d_hand)
    player_score = score_hand(p_hand)

    while dealer_score <= player_score and dealer_score < 17:
        d_hand.extend(deal_cards(1))
        dealer_score = score_hand(d_hand)
        if dealer_score > 21:
            end_game(True, p_hand, d_hand)

    return d_hand


def start_game():

    clear_screen()
    print_logo()

    global deck
    deck = gen_deck()

    player_hand = deal_cards(2)
    dealer_hand = deal_cards(2)

    player_score = score_hand(player_hand)
    dealer_score = score_hand(dealer_hand)

    if player_score == 21:
        print("BLACK JACK")
        end_game(True, player_hand, dealer_hand)
    elif dealer_score == 21:
        print("Dealer BLACK JACK")
        end_game(False, player_hand, dealer_hand)

    return player_hand, dealer_hand


def end_game(player_won, p_hand, d_hand):
    if player_won is True:
        cond = "You Won!"
    elif player_won is False:
        cond = "You lost."
    else:
        cond = "It's a tie."

    d_cards = "  ".join([decode_card(x) for x in d_hand])
    p_cards = "  ".join([decode_card(x) for x in p_hand])

    clear_screen()

    print(f"""
Dealer Hand:  ({score_hand(d_hand)}) {d_cards}
Your Hand  :  ({score_hand(p_hand)}) {p_cards}
""")

    again = input(f"{cond}\nWould you like to play again? (y/n)\n > ").lower()
    if again == 'y':
        play_game()
    else:
        exit(0)


def play_game():
    """Main game loop"""

    player_hand, dealer_hand = start_game()

    player_hand = turn_loop(player_hand, dealer_hand)
    dealer_hand = dealer_loop(dealer_hand, player_hand)

    player_score = score_hand(player_hand)
    dealer_score = score_hand(dealer_hand)

    if player_score > dealer_score:
        end_game(True, player_hand, dealer_hand)
    elif dealer_score > player_score:
        end_game(False, player_hand, dealer_hand)
    else:
        end_game(None, player_hand, dealer_hand)


if __name__ == "__main__":

    play_game()
