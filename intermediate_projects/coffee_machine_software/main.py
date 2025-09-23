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
    "water": 400,
    "milk": 300,
    "coffee": 200,
}

income = 0

def is_sufficient_resources(coffee_name):
    for key in MENU[coffee_name]["ingredients"]:
        if MENU[coffee_name]["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key} 😞.")
            return False
    return True

def secret_command(user_input):
    global income
    if user_input == "off":
        exit()
    elif user_input == "report":
        for key in resources:
            print(f"{key} : {resources[key]}")
        print(f"Income = ${income:.2f} 💰")

def process_coins():
    while True:
        try:
            print("Please insert coins 🪙")
            quarter = int(input("Enter quarters: "))
            dimes = int(input("Enter dimes: "))
            nickels = int(input("Enter nickels: "))
            pennies = int(input("Enter pennies: "))
            if min(quarter, dimes, nickels, pennies) < 0:
                print("Coin counts cannot be negative ❌.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter whole numbers ❌.")

    dollars = quarter*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return dollars

def money_transaction(dollars, coffee_name):
    global income
    cost = MENU[coffee_name]["cost"]

    if dollars >= cost:
        return_money = dollars - cost
        income += cost
        return return_money
    else:
        print("Sorry that's not enough money 💸. Money refunded.")
        return None

def resource_management(coffee_name):
    for key in MENU[coffee_name]["ingredients"]:
        resources[key] -= MENU[coffee_name]["ingredients"][key]

def coffee_machine():
    while True:
      
        user_input = input("What would you like? espresso/latte/cappuccino (1/2/3): ")

        if user_input in ["off", "report"]:
            secret_command(user_input)
            continue

        if user_input == "1":
            user_input = "espresso"
        elif user_input == "2":
            user_input = "latte"
        elif user_input == "3":
            user_input = "cappuccino"
        else:
            print("Please enter correct number")
            continue

        
        if user_input in MENU:
            if is_sufficient_resources(user_input):
                cost = MENU[user_input]['cost']
                print(f"The cost is ${cost:.2f} 💵")
                dollars = process_coins()
                return_money = money_transaction(dollars, user_input)
                if return_money is None:
                    continue
                elif return_money > 0:
                    print(f"Take ${return_money:.2f} back 💰")
                resource_management(user_input)
                print(f"Here is your {user_input} ☕. Enjoy! 😄")
        else:
            print("Invalid choice, please select espresso, latte, or cappuccino ⚠️.")

coffee_machine()  
