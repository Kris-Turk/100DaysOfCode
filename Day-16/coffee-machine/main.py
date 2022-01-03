from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()

moneymachine = MoneyMachine()

menu = Menu()

coffee_machine_on = True

while coffee_machine_on == True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'off':
        coffee_machine_on = False
    elif user_input == 'report':
        coffeemaker.report()
        moneymachine.report()
    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        menuitem = menu.find_drink(user_input)
        if coffeemaker.is_resource_sufficient(menuitem):
            if moneymachine.make_payment(menuitem.cost):
                coffeemaker.make_coffee(menuitem)
        else:
            print('Not Enough Resources to make that drink')
    else:
        print("That was not a valid selection")
            