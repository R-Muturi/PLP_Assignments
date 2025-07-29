num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    answer = num_1 + num_2
elif operation == '-':
    answer = num_1 - num_2
elif operation == '*':
    answer = num_1 * num_2
elif operation == '/':
    # Add a check for division by zero
    if num_2 != 0:
        answer = num_1 / num_2
    else:
        answer = "Error: Division by zero is not allowed."
else:
    answer = "Error: Invalid operation."

print(answer)