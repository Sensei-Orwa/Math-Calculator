# Write a simple calculator program that takes two numbers and an operation (+, -, *, /) as input and performs the calculation.

#parameters
num1 = int(input("Enter first number: "))
operator = input("Enter an Operator: ")
num2 = int(input("Enter a second number: "))


#Logic
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

else:
    result = num1 / num2

print(f"The answer is {result:.2F}")






