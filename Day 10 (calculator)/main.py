import assets
import os
clear = lambda: os.system("cls")
clear()


def add(number1, number2):
    return number1 + number2
def subtract(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    return number1 / number2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    continue_calculation = True
    while(continue_calculation):
         symbol = input("Pick an operation: ")
         choice_of_operation = operations[symbol]
        
         num2 = float(input("What's the next number?: "))
         result = choice_of_operation(num1, num2)
         print(f"{num1} {symbol} {num2} = {result}")
         more_calculations = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
         if(more_calculations == 'y'):
             num1 = result
         else:
             continue_calculation = False
             clear()
    calculator()
calculator()

