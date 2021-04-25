from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

from sys import exit


def power_off():
    """Power off the machine"""

    print("Powering off now.")
    exit(0)


def print_menu(menu):
    """Print available drinks w/ prices"""

    drinks = [item for item in menu.get_items().split('/') if item != '']

    for i in drinks:
        line = f"{menu.find_drink(i).name:15} ${menu.find_drink(i).cost:.2f}"
        print(line)


def get_selection(menu, mm):

    while True:

        print()
        print_menu(menu)

        selection = input("\nChoose a drink > ")

        if selection == 'off':
            power_off()

        elif selection == 'report':
            print()
            coffee_machine.report()
            mm.report()
            print()

        else:
            drink = menu.find_drink(selection)

            if type(drink) is MenuItem:
                if mm.make_payment(drink.cost):
                    return drink


if __name__ == '__main__':

    menu = Menu()
    coffee_machine = CoffeeMaker()
    mm = MoneyMachine()

    while True:
        selection = get_selection(menu, mm)

        if coffee_machine.is_resource_sufficient(selection):
            coffee_machine.make_coffee(selection)
