MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "profit": 0,
}


coins = {
    "quarters": 0.25,
    "dimes":  0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

coffee_choice = ""
totalinput = 0
total = 0
change = 0

# TODO: 1 “What would you like? (espresso/latte/cappuccino):”
def ask_coffee():
    return input("What would you like? (espresso/latte/cappuccino):\n").lower()


def process_coins():
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    pennies = float(input("How many pennies: "))
    totals = coins["quarters"] * quarters + coins["dimes"]*dimes + coins["nickles"]*nickles+coins["pennies"]*pennies
    return totals

while coffee_choice != "off":
    # TODO: 2 Turn off the f":Coffee Machine by entering “off” to the prompt
    coffee_choice = ask_coffee()
    if coffee_choice == "off":
        exit()
    # TODO: 3  Print report.
    elif coffee_choice == "report":

        print(f" Water:  {resources["water"]}\n Milk:   {resources["milk"]}\n Coffee: {resources["coffee"]}\n profit: ${resources["profit"]}")
    # TODO: 4 Check resources sufficient?
    if coffee_choice == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
            print("We've refunded all your coins because we ran out of water")
            exit()
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            print("We've refunded all your coins because we ran out of coffee")
            exit()
    elif coffee_choice == "latte":
        if MENU["latte"]["ingredients"]["water"] > resources["water"]:
            print("We've refunded all your coins because we ran out of water")
            exit()
        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
            print("We've refunded all your coins because we ran out of milk")
            exit()
        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            print("We've refunded all your coins because we ran out of coffee")
            exit()
    elif coffee_choice == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
            print("We've refunded all your coins because we ran out of water")
            exit()
        elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
            print("We've refunded all your coins because we ran out of milk")
            exit()
        elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
            print("We've refunded all your coins because we ran out of coffee")
            exit()
    # TODO: 5 Process coins.
    if coffee_choice != "report":
        totalinput= process_coins()

    # TODO: 6 Check transaction successful?
        if MENU[coffee_choice]["cost"] > totalinput:
            print("The trasaction has failed, we´ve refunded all your coins")
        else:
            change = totalinput - MENU[coffee_choice]["cost"]
            rounded_change = "{:.2f}".format(change)
            print(f"Thanks for your purchase, your coffee was ${MENU[coffee_choice]["cost"]} and your change is ${rounded_change}")
            resources["profit"] += MENU[coffee_choice]["cost"]
    # TODO: 7 Make Coffee

        resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
