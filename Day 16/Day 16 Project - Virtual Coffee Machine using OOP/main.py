from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make_order = CoffeeMaker()
money_machine = MoneyMachine()

should_continue = True
while should_continue:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "report":
        make_order.report()
        money_machine.report()

    elif choice == "off":
        print("Turning machine off...")
        should_continue = False

    elif choice == "espresso":
        order = menu.find_drink(choice)
        resource = make_order.is_resource_sufficient(order)
        if resource is True:
            payment = MenuItem(choice, 50, 0, 18, 1.5)
            billing = money_machine.make_payment(payment.cost)
            if billing is True:
                make_order.make_coffee(order)

    elif choice == "latte":
        order = menu.find_drink(choice)
        resource = make_order.is_resource_sufficient(order)
        if resource is True:
            payment = MenuItem(choice, 200, 150, 24, 2.5)
            billing = money_machine.make_payment(payment.cost)
            if billing is True:
                make_order.make_coffee(order)

    elif choice == "cappuccino":
        order = menu.find_drink(choice)
        resource = make_order.is_resource_sufficient(order)
        if resource is True:
            payment = MenuItem(choice, 250, 50, 24, 3)
            billing = money_machine.make_payment(payment.cost)
            if billing is True:
                make_order.make_coffee(order)

    else:
        print("Wrong Input!")


