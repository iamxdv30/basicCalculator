from Operators.Operator import Operator
import keyboard
import math

performBasicOperation = Operator.performBasicOperation
performAdvanceOperation = Operator.performAdvanceOperation
performTrigOperation = Operator.trigonometryOperation
validBasicOperators = ["+", "-", "*", "/"]
userInput = input("Enter a number, +, -, *, /, sin, cos, tan, cot, log, mod, power, 'pi', or 'exit' to quit: ").strip().lower()

def getFloatInput(prompt):
    while True:
        input_str = input(prompt).strip().lower()
        if input_str.replace('.', '', 1).isdigit() or (input_str.startswith('-') and input_str[1:].replace('.', '', 1).isdigit()):
            return float(input_str)
        else:
            print("Invalid input. Please enter a valid number.")


def userChoosePi():

    while True:

        if userInput == 'exit':
            print("Exiting the program.")
            break

        if userInput == 'pi' and not (userInput.isdigit() or performBasicOperation or performTrigOperation):
            return math.pi    
        elif userInput == 'pi':
            num1 = math.pi
        elif userInput.replace('.', '', 1).isdigit():
            num1 = float(userInput)
        elif userInput in ["sin", "cos", "tan", "cot"]:
            print("from elif statement")
            num1 = getFloatInput("Enter the angle in degrees (for trigonometric operations): ")
            trigResult = performTrigOperation(userInput, num1)
            print("Current Trigonometric result:", trigResult)
        elif userInput == 'log':
            num1 = getFloatInput("Enter a log number: ")
            num2 = getFloatInput("Enter the base: ")
            logResult = performAdvanceOperation(userInput, num1, num2)
            print("Current log result:", result)
        else:
            print("Invalid input. Please enter a number, 'pi', or 'exit'.")
            continue

        while True:
            
            chooseOperator = input("Enter an operator (+, -, *, /, sin, cos, tan, cot, log, mod, power, pi or 'back' to change number): ").strip().lower()
            if chooseOperator == 'back':
                break

            if chooseOperator in ["+", "-", "*", "/"]:
                if trigResult is not None:
                    num1 = trigResult
                    trigResult = None 
                num2 = getFloatInput("Enter another number: ")
                result = performBasicOperation(chooseOperator, num1, num2)
            elif chooseOperator in ["sin", "cos", "tan", "cot"]:
                num2 = getFloatInput("Enter the angle in degrees: ")
                result = performAdvanceOperation(chooseOperator, num1, num2)
            elif chooseOperator == "log":
                num2 = getFloatInput("Enter a number: ")
                result = performAdvanceOperation(chooseOperator, num1, num2)
            else:
                num1 = result * math.pi
                print(f'Current result: {math.pi}')
                print("Printing from else statement")
                continue
            
            if result is not None:
                print("Printing in the if statement")
                print("Current result:", result)
                num1 = result



def main():
    userChoosePi()

if __name__ == "__main__":
    main()


def choose_digit_and_basic_operator():
    while True:

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
                if chooseOperator in ["+", "-", "*", "/", "mod", "power"]:
                    num2 = getFloatInput("Enter another number: ")
                    result = performBasicOperation(chooseOperator, num1, num2)
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