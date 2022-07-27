inventory = {
    "Water": 300,
    "Coffee": 100,
    "Milk": 200,
    "Money": 0
}

MENU = {
    "espresso": {
        "Water": 50,
        "Coffee": 18,
        "Milk": 0,
        "Price": 1.50
    },
    "latte": {
        "Water": 200,
        "Coffee": 24,
        "Milk": 150,
        "Price": 2.50
    },
    "cappuccino": {
        "Water": 250,
        "Coffee": 24,
        "Milk": 100,
        "Price": 3.00
    }
}

COINS = {
    "Quarter": 0.25,
    "Dime": 0.10,
    "Nickel": 0.05,
    "Penny": 0.01
}


def print_report():
    print(f"Water: {inventory['Water']}ml")
    print(f"Milk: {inventory['Milk']}ml")
    print(f"Coffee: {inventory['Coffee']}g")
    print(f"Money: ${inventory['Money']}")


def get_change(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters * COINS["Quarter"]
    total += dimes * COINS["Dime"]
    total += nickels * COINS["Nickel"]
    total += pennies * COINS["Penny"]

    return total


def update_resources(drink_resources):
    inventory["Water"] -= drink_resources["Water"]
    inventory["Milk"] -= drink_resources["Milk"]
    inventory["Coffee"] -= drink_resources["Coffee"]


def make_drink(drink_choice):
    if drink_choice["Water"] > inventory["Water"] or drink_choice["Milk"] > inventory["Milk"] or \
            drink_choice["Coffee"] > inventory["Coffee"]:
        return False
    else:
        update_resources(drink_choice)
        return True


machine_off = False
while not machine_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_off = True
    elif user_choice == "report":
        print_report()
    else:
        if user_choice not in MENU:
            print("That drink is not in the menu. Choose again.")
        else:
            drink = MENU[user_choice]
            print("Please insert coins.")
            number_quarters = int(input("How many quarters?: "))
            number_dimes = int(input("How many dimes?: "))
            number_nickels = int(input("How many nickels?: "))
            number_pennies = int(input("How many pennies?: "))
            money = get_change(number_quarters, number_dimes, number_nickels, number_pennies)
            if money < drink["Price"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if make_drink(drink):
                    if money == drink["Price"]:
                        inventory["Money"] += money
                        print("You gave exact change. No change given.")
                        print(f"Here is your {user_choice}. Enjoy!")
                    elif money > drink["Price"]:
                        profit = drink["Price"]
                        change = money - profit
                        change = round(change, 2)
                        inventory["Money"] += drink["Price"]
                        print(f"Here is ${change} in change.")
                        print(f"Here is your {user_choice}. Enjoy!")
                else:
                    print("Could not make drink. Not enough resources.")