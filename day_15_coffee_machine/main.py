from menu import MENU, resources

## Initialize, define functions


def check_resources(coffee_type):
    is_enough_resources = True
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        print("Sorry, there is not enough water")
        is_enough_resources = False
    if resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee")
        is_enough_resources = False
    if coffee_type != 'espresso':
        if resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk")
            is_enough_resources = False
    return is_enough_resources    

def check_cash(coffee_type):
    
    print("Please insert coins.")
    
    quarters_qty = int(input("How many quarters?: "))
    dimes_qty   = int(input("How many dimes?: "))
    nickels_qty  = int(input("How many nickels?: "))
    pennies_qty  = int(input("How many pennies?: "))
    
    cash = (pennies_qty * 0.01) + (nickels_qty * 0.05) + (dimes_qty * 0.1) + (quarters_qty * 0.25)
    cash = round(cash,2)

    is_enough_cash = True

    if cash < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        is_enough_cash = False
    
    return cash, is_enough_cash


def update_resources(coffee_type):
    resources["water"] = resources["water"] - MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
    
    if coffee_type != "espresso":
        resources["milk"] = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]


def update_earnings(coffee_type,earnings):
    earnings += MENU[coffee_type]["cost"]
    return earnings


def print_report():
    print("Water: ", resources["water"], "ml", sep="")
    print("Milk: ", resources["milk"], "ml", sep="")
    print("Coffee: ", resources["coffee"], "g", sep="")
    print(f"Money: ${earnings}")


## MAIN
is_continue = True
earnings = 0

while is_continue:

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "report":
        print_report()

    else:
        coffee = user_input

        is_enough_resources = check_resources(coffee)

        if is_enough_resources == False:
            quit()
        else:
            cash, is_enough_cash = check_cash(coffee)
            if is_enough_cash == False:
                quit()
            else:
                update_resources(coffee)
                earnings = update_earnings(coffee,earnings)
                
                change = cash - MENU[coffee]["cost"]
                if change > 0:
                    print(f"Here is ${change} in change.") 
                print(f"Here is your {coffee}. Enjoy!") #TODO Add emoji for coffee
        
    











