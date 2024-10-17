from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_items = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True
while machine_on is True:
    choice = input(f"What would you like? ({menu_items.get_items()}): ").lower()
    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu_items.find_drink(choice)
        make_drink = coffee_machine.is_resource_sufficient(drink)
        if make_drink is True:
            sufficient_transaction = money_machine.make_payment(drink.cost)
            if sufficient_transaction is True:
                coffee_machine.make_coffee(drink)





