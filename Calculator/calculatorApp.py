import calculator

first_number = int(input("Please enter the 1st number: "))
operand = input("Please enter the operand: ")
second_number = int(input("Please enter the 2nd number: "))

if operand == "+":
    print(f"The sum of {first_number} and {second_number} is {calculator.add(first_number,second_number)}")
elif operand == "-":
    print(f"The result of subracting {first_number} and {second_number} is {calculator.subtract(first_number,second_number)}")
elif operand == "*":
    print(f"The result of multiplying {first_number} and {second_number} is {calculator.multiply(first_number,second_number)}")
elif operand == "/":
    print(f"The result of dividing {first_number} and {second_number} is {calculator.divide(first_number,second_number)}")
else:
    print("Operand must be +, -, *, or /. Please try again.")
