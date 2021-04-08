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
}


def make_coffe(coffe_type):
    if coffe_type == "":
        exit()
    water_use = MENU[coffe_type]['ingredients']['water']
    coffee_use = MENU[coffe_type]['ingredients']['coffee']
    if coffe_type == "espresso":
        milk_use = 0
    else:
        milk_use = MENU[coffe_type]['ingredients']['milk']
    coffee_cost = MENU[coffee_type]['cost']
    return [water_use, milk_use, coffee_use, coffee_cost]


def money():
    print("Please, insert coins.")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))
    total_amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(total_amount)


def water():
    water_left = int(resources['water'])
    water_use = int(make_coffe(coffee_type)[1])
    water_left = water_left - water_use
    if water_left < 0:
        print("Not enough water to make your coffee")
        exit()
    else:
        resources['water'] = water_left


while True:
    entered_text = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if entered_text == "report":
        print(resources)
        coffee_type = ""
    elif entered_text == "off":
        exit()
    else:
        coffee_type = entered_text

    water()

    print(resources)
    print(money())




