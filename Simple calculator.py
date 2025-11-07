# simple calculator
# Ask user for input
num1 = float(input("Enter your first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter your second number: "))

# perform calculation based on operator
if operator == '+':
    result = num1+num2
elif operator == '-':
    result = num1-num2
elif operator == '*':
    result = num1*num2
elif operator == '/':
    if num2 !=0:
        result= num1/num2
    else:
        result = "ERROR!! Division by 0."
else:
    result = "Invalid Operator."

print("Result: ", result) 