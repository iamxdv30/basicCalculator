from Operators.Operator import Operator
import keyboard
import math

performBasicOperation = Operator.performBasicOperation
performAdvanceOperation = Operator.performAdvanceOperation
performTrigOperation = Operator.trigonometryOperation
validBasicOperators = ["+", "-", "*", "/"]

def getFloatInput(prompt):
    while True:
        input_str = input(prompt).strip().lower()
        if input_str.replace('.', '', 1).isdigit() or (input_str.startswith('-') and input_str[1:].replace('.', '', 1).isdigit()):
            return float(input_str)
        else:
            print("Invalid input. Please enter a valid number.")

def calculator():
    num1 = None
    result = None
    while True:
        if num1 is None:
            userInput = input("Enter a number, +, -, *, /, sin, cos, tan, cot, log, mod, power, 'pi', or 'exit' to quit: ").strip().lower()

            if userInput == 'exit':
                print("Exiting the program.")
                break
            elif userInput == 'pi':
                num1 = math.pi
            elif userInput.replace('.', '', 1).isdigit():
                num1 = float(userInput)
            elif userInput in ["sin", "cos", "tan", "cot"]:
                angle = getFloatInput("Enter the angle in degrees (for trigonometric operations): ")
                num1 = performTrigOperation(userInput, angle)
                print("Current Trigonometric result:", num1)
            elif userInput == 'log':
                number = getFloatInput("Enter a log number: ")
                base = getFloatInput("Enter the base: ")
                num1 = math.log(number, base)
                print("Current log result:", num1)
            else:
                print("Invalid input. Please enter a valid number, 'pi', or 'exit'.")
                continue

        chooseOperator = input("Enter an operator (+, -, *, /, sin, cos, tan, cot, log, mod, power, pi or 'back' to change number): ").strip().lower()
        if chooseOperator == 'back':
            num1 = None
            continue
        elif chooseOperator in ["+", "-", "*", "/"]:
            num2 = getFloatInput("Enter another number: ")
            result = performBasicOperation(chooseOperator, num1, num2)
        elif chooseOperator in ["sin", "cos", "tan", "cot"]:
            angle = getFloatInput("Enter a digit in degrees: ")
            result = performAdvanceOperation(chooseOperator, num1, angle)
        elif chooseOperator == "log":
            number = getFloatInput("Enter a number: ")
            base = getFloatInput("Enter the base: ")
            result = performAdvanceOperation(chooseOperator, number, base)
        else:
            print("Invalid operator. Please try again.")
            continue

        if result is not None:
            print("Current result:", result)
            num1 = result

def main():
    calculator()

if __name__ == "__main__":
    main()

