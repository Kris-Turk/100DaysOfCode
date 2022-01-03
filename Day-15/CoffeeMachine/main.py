MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

#  Take user Input
def start():
    """Requests input from user and returns as a string

    Returns:
        String: Description
    """
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

#  Print Report
def print_report():
    print(f"""
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}""")
    
# Check Resources pre dispensing

def check_resources(user_input):
    """Takes user input and checks the menu item against available resources
    """
    for i in MENU[user_input]['ingredients']:
        if MENU[user_input]['ingredients'][i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False

#  Process Coins
def process_coins():
    """Takes user input in number of each coin denomiation and returns the total monetary value

    Returns:
        int: [description]
    """
    print("Please insert coins.")    
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return money

# Check Transaction is successful

def process_transaction(money,user_input):
    global resources
    if money < MENU[user_input]['cost']:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif money == MENU[user_input]['cost']:
        resources["money"] += MENU[user_input]['cost']
        return True
    else:
        resources["money"] += MENU[user_input]['cost']
        change = round((money - MENU[user_input]['cost']),2)
        print(f"Here is ${change} dollars in change")
        return True            

#  Make Coffee and Deduct resources

def make_coffee(user_input):
    global resources
    for i in MENU[user_input]['ingredients']:
        resources[i] -= MENU[user_input]['ingredients'][i]
    print(f"Here is you {user_input}. Enjoy!")    
    
def coffee_machine():
    user_input = start()
    if user_input == 'report':
        print_report()
        coffee_machine()
    elif user_input == 'off':
        return
    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        resource_check = check_resources(user_input)
        if resource_check != False:
            money = process_coins()
            transaction = process_transaction(money,user_input)
            if transaction:
                make_coffee(user_input)
        coffee_machine()
    else:
        print("That was not a valid Selection")
        coffee_machine()  
  
coffee_machine()