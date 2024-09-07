from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the Coffee Machine!")
is_on = True
coffee_machine = CoffeeMaker()
menu = Menu()
MoneyMachine = MoneyMachine()

while is_on:
    options = menu.get_items()
    coffee = input(f"What would you like to have? ({options}): ")

    if coffee == "off":
        print("Thankyou for using the machine. Visit again!!")
        is_on = False
    elif coffee == "report":
        coffee_machine.report()
        MoneyMachine.report()
    else:
        drink = menu.find_drink(coffee)
        if coffee_machine.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
             coffee_machine.make_coffee(drink)

