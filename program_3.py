# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
#check which category the user's input falls into and assign the correct dollar amount to shippingCost
    if weight <= 2 and weight > 0:
        shippingCost = 1.5
    elif weight > 2 and weight < 6:
        shippingCost = 3
    elif weight >= 6 and weight < 10:
        shippingCost = 4
    elif weight >= 10:
        shippingCost = 4.75
    # if all conditions fail the user's input was invalid
    else:
        print("invalid weight")
    
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $' + format(shippingCost, '.2f'))