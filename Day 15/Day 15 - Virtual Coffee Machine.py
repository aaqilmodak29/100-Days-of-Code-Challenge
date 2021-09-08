MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    },
    "should_continue": {
        "bool": True
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

money = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

total = 0


def resource(choice):
    if choice == "espresso":
        water_required = MENU["espresso"]["ingredients"]["water"]
        coffee_required = MENU["espresso"]["ingredients"]["coffee"]
        # if resources["water"] < water_required:
        #     print("Not enough water")
        #     MENU["should_continue"]["bool"] = False
        # elif resources["coffee"] < coffee_required:
        #     print("Not enough coffee")
        #     MENU["should_continue"]["bool"] = False
        resources["water"] -= water_required
        resources["coffee"] -= coffee_required

    elif choice == "latte" or choice == "cappuccino":
        water_required = MENU[choice]["ingredients"]["water"]
        coffee_required = MENU[choice]["ingredients"]["coffee"]
        milk_required = MENU[choice]["ingredients"]["milk"]
        # if resources["water"] < water_required:
        #     print("Not enough water")
        #     MENU["should_continue"]["bool"] = False
        #     return
        # elif resources["coffee"] < coffee_required:
        #     print("Not enough coffee")
        #     MENU["should_continue"]["bool"] = False
        #     return
        #
        # elif resources["milk"] < milk_required:
        #     print("Not enough milk")
        #     MENU["should_continue"]["bool"] = False
        resources["water"] -= water_required
        resources["coffee"] -= coffee_required
        resources["milk"] -= milk_required


def payment(choice, total_money):
    cost = MENU[choice]["cost"]
    print("Please insert coins: ")
    quarters_spent = int(input("How many quarters?: "))
    dimes_spent = int(input("How many dimes?: "))
    nickels_spent = int(input("How many nickels?: "))
    pennies_spent = int(input("How many pennies?: "))

    quarters_spent_total = quarters_spent * money["quarters"]
    dimes_spent_total = dimes_spent * money["dimes"]
    nickels_spent_total = nickels_spent * money["nickels"]
    pennies_spent_total = pennies_spent * money["pennies"]

    total_spent = quarters_spent_total + dimes_spent_total + nickels_spent_total + pennies_spent_total
    if total_spent < cost:
        print("Sorry, you didn't deposit enough money. Money refunded")
    elif total_spent > cost:
        resource(choice)
        change = total_spent - cost
        rounded_change = round(change, 2)
        print(f"Here is ${rounded_change} in change.")
        print(f"Here is your {choice}. Enjoy!")
        total_money += rounded_change
        resources["money"] += MENU[choice]["cost"]


def espresso(choice):
    payment(choice, total)
    # resource(choice, should_continue)


def latte(choice):
    payment(choice, total)
    # resource(choice, should_continue)


def cappuccino(choice):
    payment(choice, total)
    # resource(choice, should_continue)


while MENU["should_continue"]["bool"] == True:
    coffee_choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
    if coffee_choice == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}")
    elif coffee_choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Not enough water for espresso")
            # MENU["should_continue"]["bool"] = False
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Not enough coffee for espresso")
            # MENU["should_continue"]["bool"] = False
        else:
            espresso(coffee_choice)

    elif coffee_choice == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Not enough water for latte")
            if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                print("Not enough water for an espresso")
                # MENU["should_continue"]["bool"] = False

        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Not enough milk for latte")
            # MENU["should_continue"]["bool"] = False

        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Not enough coffee for latte")
            if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                print("Not enough coffee for an espresso")
                # MENU["should_continue"]["bool"] = False

        else:
            latte(coffee_choice)

    elif coffee_choice == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Not enough water for cappuccino")
            if resources["water"] < MENU["latte"]["ingredients"]["water"]:
                print("Not enough water for a latte")
            elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                print("Not enough water for an espresso")
                # MENU["should_continue"]["bool"] = False

        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Not enough milk for cappuccino")
            if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
                print("Not enough milk for a latte")
            else:
                MENU["should_continue"]["bool"] = False

        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Not enough coffee for cappuccino")
            if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
                print("Not enough water for a latte")
            elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                print("Not enough water for an espresso")
                # MENU["should_continue"]["bool"] = False
        else:
            cappuccino(coffee_choice)
    elif coffee_choice == "off":
        MENU["should_continue"]["bool"] = False
    else:
        print("Wrong Input!")

