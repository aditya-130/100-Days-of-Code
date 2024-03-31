import data

def get_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = (quarters * 0.25) + (nickels * 0.05) + (dimes * 0.1) + (pennies * 0.01)
    return total_amount

def update_ingredients(resources, ingredients):
    initial_resources = resources.copy()
    for item in ingredients:
        if item in resources:
            if resources[item] >= ingredients[item]:
                resources[item] = resources[item] - ingredients[item]
            else:
                print(f"Sorry there's not enough {item}")
                return initial_resources, False
    return resources, True


def update_money(resources, cost):
    if "money" in resources:
        resources["money"] =  f"${str(float(resources["money"][1:] )+ cost)}"
    else:
        resources["money"] = f"${str(cost)}"
    return resources

def order_coffee_and_update_resources(coffee_type, resources):
    menu_items = data.MENU
    initial_resources = resources.copy()
    ingredients = menu_items[coffee_type]["ingredients"]
    cost = menu_items[coffee_type]["cost"]
    balance = 0
    resources, enough_ingredients = update_ingredients(resources, ingredients)
    if enough_ingredients:
        user_payment = get_money()
        if user_payment > cost:
            balance = "{:.2f}".format(round(user_payment - cost, 2))
            print(f"Here's your change: ${balance}")
        elif user_payment < cost:
            print("Insufficient funds\n")
            return initial_resources
        print(f"Here's your {coffee_type}")
        return update_money(resources, cost)
    print()
    return initial_resources
    
def display_report(resourses):
    for resourse in resources:
        print(f"{resourse}: {resources[resourse]}")

resources = data.resources
coffe_machine_runnning = True
while coffe_machine_runnning:
    user_choice =  input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        display_report(resources)
    elif user_choice in ["espresso", "latte", "cappuccino"]:
       resources =  order_coffee_and_update_resources(user_choice, resources)
    else:
        print("Invalid input")