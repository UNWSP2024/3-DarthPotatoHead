#Program Written By: Ainsley Bellamy
#Date Written: 01/27/2025
#Program Title: Bloated_HotDog_Program

#Halfway through writing this, my dad came in a told me about dictionaries.

# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

#This function appears first because I needed it pre-defined so that I could call it later.
def add_toppings(topping_total):
#This 'x' variable controls how long the loop runs.
    x = 0
#I defined the starting total and the cost of each topping.
    total = 0
    cheese = .50
    peppers = .75
    grilled_onions = 1
#This while loop runs through the user input string, which I
# split, adding the cost of each item if it finds it.
    while x < len(topping_total):
        if topping_total[x] == 'cheese':
            total = total + cheese
        elif topping_total[x] == 'peppers':
            total = total + peppers
        elif topping_total[x] == 'grilled_onions':
            total = total + grilled_onions
        else:
            print("You did not enter a valid answer. No Hot Dog for you.")
        x = x+1
#Returns the total cost of toppings to the variable 'toppings_cost,' which is
# defined and called in the next function.
    return total

#New function to first determine hot dog type and then call previous 'add_toppings()' function.
def hotdog_cost():
    hotdog_cost = 0.0
    initial_order = str(input("Would you like a Regular Hot Dog or a Chili Dog? "))
    if initial_order.lower() == 'regular hot dog':
        hotdog_cost = 3.5
        additions = str(input("Would you like to add additional toppings? "))
        if additions == 'yes':
            toppings = str(input("Select topping(s) (Toppings "
                                 "include: Cheese $0.50, Peppers $0.75, and Grilled Onions $1.00) "
                                 "[Example = 'peppers grilled_onions']: ")).split()
            add_toppings(toppings)
        else:
# Print out the results early, with no added cost from toppings.
            print(f"Subtotal: ${hotdog_cost:.2f}\n"
                  "Tax Amount: $" + format(hotdog_cost * .07, '.2f'),"\n"
                  "Total (Plus Tax): $" + format(hotdog_cost * .07 + hotdog_cost, '.2f'))
            return
    elif initial_order.lower() == 'chili dog':
        hotdog_cost = 4.5
        additions = str(input("Would you like to add additional toppings? "))
        if additions == "yes":
            toppings = str(input("Select topping(s) (Toppings "
                                 "include: Cheese $0.50, Peppers $0.75, and Grilled Onions $1.00) "
                                 "[Example = 'peppers grilled_onions']: ")).split()
            add_toppings(toppings)
        else:
#Print out the results early, with no added cost from toppings.
            print(f"Subtotal: ${hotdog_cost:.2f}\n"
                  "Tax Amount: $" + format(hotdog_cost * .07, '.2f'),"\n"
                  "Total (Plus Tax): $" + format(hotdog_cost * .07 + hotdog_cost, '.2f'))
            return
#If all conditions fail, program just ends.
    else:
        print("You did not enter a valid answer. No Hot Dog for you.")
        return
#This is the result from the function 'add_toppings()'.
    toppings_cost = add_toppings(toppings)
#Now defining tax rate, amount, subtotal, and total.
    subtotal = toppings_cost + hotdog_cost
    tax_rate = .07
    tax_amount = subtotal * .07
    total = tax_amount + subtotal
    print(f"Subtotal (Hot Dog + Toppings): ${subtotal:.2f}\n"
          f"Tax Amount: ${tax_amount:.2f}\n"
          f"Total (Plus Tax): ${total:.2f}")
hotdog_cost()