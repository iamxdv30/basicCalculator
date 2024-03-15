from basic_Op.basicOperator import basicOperator
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
        return num1 / num2
    else:
        print("Invalid operation")
        return num1
    
def performAdvanceOperation(operator, num1, num2, log_base=10):
    angleInRadians = math.radians(num2) if operator in ['sin', 'cos', 'tan', 'cot'] else None
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
        return num1
    
def getFloatInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    userInput = input("Enter a number, +, -, *, /, sin, cos, tan, cot, log, mod, power, 'pi', or 'exit' to quit: ").strip().lower()
    while True:
        if userInput == 'exit':
            break
        if userInput.isdigit():
            num1 = float(userInput)
            while True:
                chooseOperator = input("Enter an operator (+, -, *, /, sin, cos, tan, cot, log, mod, power, pi or 'back' to change number): ").strip().lower()
                if chooseOperator == 'back':
                    break
                if chooseOperator in ["+", "-", "*", "/"]:
                    num2 = getFloatInput("Enter another number: ")
                    result = performBasicOperation(chooseOperator, num1, num2)
                elif chooseOperator in ["sin", "cos", "tan", "cot", "log", "mod"]:
                    num2 = getFloatInput("Enter another number: ")
                    if chooseOperator == "log":
                        base = getFloatInput("Enter the base: ")
                        result = performAdvanceOperation(chooseOperator, num1, num2, base)
                    else:
                        result = performAdvanceOperation(chooseOperator, num1, num2)
                else:
                    print("Invalid operation.")
                    continue
                print("Current result:", result)
                num1 = result
        
        if userInput == 'pi':
            num1 = math.pi
        if userInput == 'power':
            num1 = getFloatInput("Enter the base: ")
            num2 = getFloatInput("Enter the exponent: ")
            result = performAdvanceOperation(userInput, num1, num2)
            print("Current result:", result)
        if userInput == 'exit':
            break
        if userInput in ["sin", "cos", "tan", "cot"]:
            num1 = getFloatInput("Enter the angle in degrees: ")
            result = performAdvanceOperation(userInput, num1, None)
            print("Current result:", result)
        if userInput in ["log", "mod"]:
            num1 = getFloatInput("Enter the number: ")
            num2 = getFloatInput("Enter the base: ")
            result = performAdvanceOperation(userInput, num1, num2)
            print("Current result:", result)
        
        else:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")
            continue

if __name__ == "__main__":
    main()
