# Simple Input and Output in Python

# Ask the user to enter their name
name = input("Enter your name: ")  # input() gets user input as a string

# Print a greeting message using the input
print("Hello,", name)  # print() outputs text to the screen

# Ask the user to enter their age
age = input("Enter your age: ")

# Print a message with the user's age
print("You are", age, "years old.")


var = int(input("Enter an Number: "))  # Convert input to integer
print("You entered the Number:", var)
flt = float(input("Enter a floating-point number: "))  # Convert input to float
print("You entered the float:", flt)
# Demonstrating formatted output
print("Formatted output: Name: {}, Age: {}, Integer: {}, Float: {:.2f}".format(name, age, var, flt))
print(f"Formatted output using f-string: Name: {name}, Age: {age}, Integer: {var}, Float: {flt:.2f}")
