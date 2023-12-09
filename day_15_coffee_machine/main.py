from menu import MENU, resources

## Initialize, define functions

def check_resources(coffee_type):
    ''' Returns false if there is not enough resources'''
    is_enough_resources = True

    for order_reqs in MENU[coffee_type]["ingredients"]:
        if resources[order_reqs] < MENU[coffee_type]["ingredients"][order_reqs]:
            print(f"Sorry, there is not enough {order_reqs}")
            is_enough_resources = False
            
    return is_enough_resources    

def check_cash(coffee_type):
    ''' Returns the total amount of cash entered and false if there is not enough cash '''
    print("Please insert coins.")
    
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes   = int(input("How many dimes?: ")) * 0.1
    nickels  = int(input("How many nickels?: ")) * 0.05
    pennies  = int(input("How many pennies?: ")) * 0.01
    
    cash = round((quarters + dimes + nickels + pennies), 2)

    is_enough_cash = True

    if cash < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        is_enough_cash = False
    
    return cash, is_enough_cash


def update_resources(coffee_type):
    ''' Updates the amount of resources left in the machine'''
    for order_reqs in MENU[coffee_type]["ingredients"]:
        resources[order_reqs] -= MENU[coffee_type]["ingredients"][order_reqs]


def update_earnings(coffee_type,earnings):
    ''' Updates the earnings in the machine and returns the total earnings'''
    earnings += MENU[coffee_type]["cost"]
    return earnings


def print_report():
    ''' Prints latest inventory list and earnings'''
    print("Water: ", resources["water"], "ml", sep="")
    print("Milk: ", resources["milk"], "ml", sep="")
    print("Coffee: ", resources["coffee"], "g", sep="")
    print(f"Money: ${earnings}")


## MAIN Program
is_continue = True
earnings = 0

while is_continue:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        is_continue = False

    elif user_input == "report":
        print_report()

    else:
        coffee = user_input

        is_enough_resources = check_resources(coffee)

        if is_enough_resources == True:
            cash, is_enough_cash = check_cash(coffee)
            if is_enough_cash == True:
                update_resources(coffee)
                earnings = update_earnings(coffee, earnings)
                
                change = cash - MENU[coffee]["cost"]

                if change > 0:
                    print(f"Here is ${change} in change.") 
                print(f"Here is your {coffee} ☕️. Enjoy!") #TODO Add emoji for coffee
        
    











