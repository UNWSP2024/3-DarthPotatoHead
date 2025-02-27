#Program Written By: Ainsley Bellamy
#Date Written: 02/3/2025
#Program Title: Categorize_Age


# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:

# If the person is 1 year old or less, it should display "infant" (without quotes).
# If the person is older than 1 year, but younger than 13 years, it should display "child".
# If the person is at least 13 years old, but less than 20 years old, it should display "teenager".
# If the person is at least 20 year old, it should display "adult".

def categorize_age(age):
    ageCategory = "TBD"
#check which category the user's input falls into and assign a new value to ageCategory accordingly
    if (age <= 1 and age > 0):
        ageCategory = "infant"
    elif age > 1 and age < 13:
        ageCategory = "child"
    elif age >= 13 and age < 20:
        ageCategory = "teenager"
    elif age >= 20:
        ageCategory = "adult"
#if all conditions fail the user's input was invalid
    else:
        ageCategory = "invalid age number"

    return ageCategory


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)