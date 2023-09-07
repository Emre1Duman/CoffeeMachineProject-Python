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

#Resource variables
remaining_water = resources['water']
remaining_milk = resources['milk']
remaining_coffee = resources['coffee']

#Drink cost variables
espresso_price = MENU["espresso"]["cost"]
espresso_water_cost = MENU["espresso"]["ingredients"]["water"]
espresso_coffee_cost = MENU["espresso"]["ingredients"]["coffee"]
espresso_milk_cost = 0

latte_price = MENU["latte"]["cost"]
latte_water_cost = MENU["latte"]["ingredients"]["water"]
latte_coffee_cost = MENU["latte"]["ingredients"]["coffee"]
latte_milk_cost = MENU["latte"]["ingredients"]["milk"]

cappuccino_price = MENU["cappuccino"]["cost"]
cappuccino_water_cost = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_coffee_cost = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_milk_cost = MENU["cappuccino"]["ingredients"]["milk"]

def deduct_resources(water, coffee, milk):
    global remaining_water
    global remaining_coffee
    global remaining_milk
    remaining_water -= water
    remaining_coffee -= coffee
    remaining_milk -= milk
    

#Print remaining resources when typing report
def resources_left(water, milk, coffee):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")


def calculate_total_coins():
    print("Please insert coins")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))
    total = 0
    total += quarters * 0.25
    total += dimes * 0.10
    total += nickles * 0.05
    total += pennies * 0.01
    rounded_total = round(total, 2)
    return rounded_total


def calculate_change(coins, drink,):
    """Take total coins user gave, check to see if its enough, return with refund or change"""
    if coins < drink:
        return "Sorry that's not enough money. Money refunded."
    elif coins >= drink:
        change = coins - drink
        rounded_change = round(change, 2)
        return f"Here is {rounded_change} in change."


Coffe_machine_active = True

while Coffe_machine_active:
    #Input ask for type of drink
    drink = input(" What would you like? (espresso/latte/cappuccino) ").lower()
    if drink == "report":
        resources_left(remaining_water, remaining_milk, remaining_coffee)
    elif drink == "espresso":
        total_coins = calculate_total_coins()
        print(calculate_change(total_coins, espresso_price))
        deduct_resources(espresso_water_cost, espresso_coffee_cost, espresso_milk_cost)
        if total_coins >= espresso_price:
            print(f"Here is your {drink} ☕️. Enjoy!")
    elif drink == "latte":
        total_coins = calculate_total_coins()
        print(calculate_change(total_coins, latte_price))
        deduct_resources(latte_water_cost, latte_coffee_cost, latte_milk_cost)
        if total_coins >= latte_price:
            print(f"Here is your {drink} ☕️. Enjoy!")
    elif drink == "cappuccino":
        total_coins = calculate_total_coins()
        print(calculate_change(total_coins, cappuccino_price))
        deduct_resources(cappuccino_water_cost, cappuccino_coffee_cost, cappuccino_milk_cost)
        if total_coins >= cappuccino_price:
            print(f"Here is your {drink} ☕️. Enjoy!")
    elif drink == "off":
        Coffe_machine_active = False
        print("Shutting down...")