from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
cash_register = MoneyMachine()

machine_off = False
while not machine_off:
    user_choice = input(f"What would you like? {menu.get_items()}: ").lower()

    if user_choice == "off":
        machine_off = True
    elif user_choice == "report":
        coffee_maker.report()
        cash_register.report()
    elif user_choice not in menu.get_items():
        print("That is not on the menu.")
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and cash_register.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)