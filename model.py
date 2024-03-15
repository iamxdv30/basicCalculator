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
    elif operator == "**":
        return num1 ** num2
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
    elif operator == "exp":
        return num1 * math.exp(num2)
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
    while True:
        userInput = input("Enter a number, 'pi', 'e', or 'exit' to quit: ").strip().lower()
        if userInput == 'exit':
            break
        elif userInput == 'pi':
            num1 = math.pi
        elif userInput == 'e':
            num1 = math.e
        elif userInput.replace('.', '', 1).isdigit():
            num1 = float(userInput)
        else:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")
            continue

        while True:
            chooseOperator = input("Enter an operator (+, -, *, /, sin, cos, tan, cot, log, mod, exp, pi or 'back' to change number): ").strip().lower()
            if chooseOperator == 'back':
                break
            if chooseOperator in ["+", "-", "*", "/"]:
                num2 = getFloatInput("Enter another number: ")
                result = performBasicOperation(chooseOperator, num1, num2)
            elif chooseOperator in ["sin", "cos", "tan", "cot", "log", "mod", "exp", "pi"]:
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

if __name__ == "__main__":
    main()


"""
def main():
    userInput = input("Enter number, sin, cos, tan, cot, log, mod, exp, pi or 'exit' to quit: ")
    
    while True:
        if userInput == 'exit':
            break  # Exit the loop and end the program
        if userInput.isdigit():
            chooseOperator = input("Enter an operator (+, -, *, /, sin, cos, tan, cot, log, mod, exp, pi or 'exit' to quit:): ").strip()
            if chooseOperator.lower() == 'exit':
                break
            elif chooseOperator in ["+", "-", "*", "/"]:
                nthNumber = input("Enter another number or 'back' to change operation: ").strip()
                if nthNumber.lower() == 'back':
                    continue
                try:
                    nthNumber = float(nthNumber)
                    result = performBasicOperation(chooseOperator, userInput, nthNumber)
                    print("Current result:", result)
                    userInput = result  # Update num with the result for the next operation
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif chooseOperator in ["sin", "cos", "tan", "cot", "log", "mod", "exp", "pi"]:
                nthNumber = input("Enter another number or 'back' to change operation: ").strip()
                if nthNumber.lower() == 'back':
                    continue
                try:
                    nthNumber = float(nthNumber)
                    result = performAdvanceOperation(chooseOperator, userInput, nthNumber)
                    print("Current result:", result)
                    userInput = result  # Update num with the result for the next operation
                except ValueError:
                    print("Invalid input. Please enter a valid number.")           
            elif userInput == 'pi':
                userInput = math.pi
            elif userInput == 'e':
                userInput = math.e
            else:
                print("Invalid input. Please enter a valid number or 'exit' to quit.")
        else:
            print("Please enter a valid initial number or 'exit' to quit.")

if __name__ == "__main__":
    main()



"""
