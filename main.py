
PROFIT = 0
def main():
    is_on = True
    while is_on:

        choice = wwyl().lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}g")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${PROFIT}")
        elif choice in ["latte", "espresso", "cappuccino"]:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                print(f"please insert {drink['cost']}")
                change = process_coins(drink, resources)
                change = round(change,2)
                print(f"Thank you. Your change: {change}")
                resource_drainer(drink["ingredients"])
        else:
            print("Not a valid response")













def wwyl():
    choice = input("What would you like? espresso, cappuccino, or latte? ")
    return choice


def turn_off():
    return "break"


def check_resources(drink_ingredients):
    for wmc in drink_ingredients: #wmc = [water, milk, coffee]
        if (drink_ingredients[wmc]) > resources[wmc]:
            print(f"sorry, there is not enough {wmc}")
            return False
        else:
            return True

def process_coins(drink, resources):
    total_amount = 0
    coins = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}

    while total_amount < drink["cost"]:
        for coin in coins:
            amount = float((input(f"how many {coin}?")))
            total_amount += coins[coin] * amount
            if total_amount >= drink["cost"]:
                break
            # resources = resources[wmc] - drink_ingredients[wmc]
    global PROFIT
    PROFIT += drink["cost"]
    return -1*(drink["cost"] - total_amount)


# write a for loop that subtracts the drink resources from the stock resources
def resource_drainer(drink_ingredients):
    for wmc in drink_ingredients:
        resources[wmc] -= drink_ingredients[wmc]










MENU  = {
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
}


#TODO
main()

#for substance, value in drink_ingredients.items():
    # print(value)