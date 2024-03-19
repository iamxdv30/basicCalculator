from Operators.Operator import Operator
import keyboard
import math

def performBasicOperation(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            return num1
    else:
        print("Invalid operation")
        return None
    
def performAdvanceOperation(operator, num1, num2, log_base=10):
    angleInRadians = math.radians(num2) if operator in ['sin', 'cos', 'tan', 'cot'] and num2 is not None else None
    if operator == "sin":
        return num1 * math.sin(angleInRadians)
    elif operator == "cos":
        return num1 * math.cos(angleInRadians)
    elif operator == "tan":
        return num1 * math.tan(angleInRadians)
    elif operator == "cot":
        return num1 * 1 / math.tan(angleInRadians)
    elif operator == "log":
        return num1 * math.log(num2, log_base)
    elif operator == "mod":
        return num1 % num2
    elif operator == "power":
        return num1 ** num2
    elif operator == "pi":
        return num1 * math.pi
    else:
        print("Invalid operation")
        return None
    
def getFloatInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        userInput = input("Enter a number, +, -, *, /, sin, cos, tan, cot, log, mod, power, 'pi', or 'exit' to quit: ").strip().lower()
        if userInput == 'exit':
            print("Exiting program.")
            break
        if userInput.isdigit() or userInput.replace('.', '', 1).isdigit() or userInput == 'pi':
            num1 = math.pi if userInput == 'pi' else float(userInput)
            while True:
                chooseOperator = input("Enter an operator (+, -, *, /, sin, cos, tan, cot, log, mod, power, pi or 'back' to change number): ").strip().lower()
                if chooseOperator == 'back':
                    break
                num2 = None
                if chooseOperator in ["+", "-", "*", "/", "sin", "cos", "tan", "cot", "log", "mod", "power"]:
                    if chooseOperator not in ["sin", "cos", "tan", "cot", "pi"]:
                        num2 = getFloatInput("Enter another number: ")
                    if chooseOperator == "log":
                        base = getFloatInput("Enter the base: ")
                        result = performAdvanceOperation(chooseOperator, num1, num2, base)
                    else:
                        result = performBasicOperation(chooseOperator, num1, num2) if chooseOperator in ["+", "-", "*", "/"] else performAdvanceOperation(chooseOperator, num1, num2)
                    if result is not None:
                        print("Current result:", result)
                        num1 = result
                    else:
                        print("No operation performed.")
                else:
                    print("Invalid operation.")
                    continue
        else:
            print("Invalid input. Please enter a valid number, operation, or 'exit' to quit.")

if __name__ == "__main__":
    main()
