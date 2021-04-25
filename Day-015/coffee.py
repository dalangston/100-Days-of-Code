from machine_data import MENU
from machine_data import resources
from sys import exit


def get_selection():
    """Main menu"""

    selection = ""

    while True:

        selection = input(
                "What would you like? (espresso/latte/cappuccino)\n > "
                ).lower()

        if selection in MENU:
            if check_resources(MENU[selection], resources):
                if process_payment(MENU[selection]['cost']):
                    make_drink(selection)
        elif selection == "off":
            power_off()
        elif selection == "report":
            print_report()
        else:
            print("Unrecognized selection\n")


def power_off():
    """Power off machine for maintainance"""

    print("Powering off now.")
    exit(0)


def print_report():
    """Print state of machine resources"""

    print(f"""
Current Resources
-----------------
Water :  {resources['water']} ml
Milk  :  {resources['milk']} ml
Coffee:  {resources['coffee']} g
Money :  $ {resources['money']:.2f}
""")


def check_resources(receipe, resources):
    """Check that there are enough resources to make selection"""

    resources_available = True

    for ingredient, required_amount in receipe['ingredients'].items():
        if resources[ingredient] < required_amount:
            print(f"Insufficient {ingredient}")
            resources_available = False

    return resources_available


def process_payment(price):
    """Get coins and check amount against price"""

    print(f"Deposit coins:  ${price:.2f}")

    # TODO:  validate input
    quarters = int(input("How many Quarters?  "))
    dimes = int(input("How many Dimes?  "))
    nickels = int(input("How many Nickels?  "))
    pennies = int(input("How many Pennies?  "))

    deposit = (
            (quarters * 0.25) + (dimes * 0.10) +
            (nickels * 0.05) + (pennies * 0.01)
            )

    if deposit == price:
        resources['money'] += deposit
        return True
    elif deposit < price:
        print("Sorry, that's not enough.  Mony refunded.")
        return False
    else:
        if resources['money'] >= (deposit - price):
            print(f"Change returned;  ${deposit - price:.2f}")
            resources['money'] += (deposit - price)
            return True
        else:
            print("No change available.  Money refunded")
            return False


def make_drink(selection):
    """Make drink, update resources"""

    for k, v in MENU[selection]['ingredients'].items():
        resources[k] -= v

    print(f"Here is your {selection}. Enjoy!")


if __name__ == "__main__":

    resources['money'] = 0
    get_selection()
