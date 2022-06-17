from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    choice = input(f"What would you like: ({menu.get_items()})?: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)


# drink_ingredients = menu.find_drink(choice).ingredients
#
#
#
# print(menu.find_drink(choice).ingredients)
# print(menu.find_drink(choice).cost)

# menu = Menu()
# menu_item = MenuItem()

# money_machine.make_payment(5)
