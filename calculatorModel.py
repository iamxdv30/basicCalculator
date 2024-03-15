from basic_Op.basicOperator import basicOperator
import keyboard
import math


num1 = input("Enter here: ")
basicOrAdvance = input("Enter basic or advance: ")

def selectBasicOrAdvance(num1, basicOrAdvance):
    if basicOrAdvance == "basic":
        while True:
            if keyboard.is_pressed('esc'):
                print("Esc key pressed, exiting...")
                break  # Exit the loop if Esc is pressed
            
            chooseBasicOperator = input("Enter +, -, *, /, **: ")
            nthNumber = input("Enter another number: ")
            basicCalculate = basicOperator()
            result = 0

            if chooseBasicOperator == "+":
                result = basicCalculate.useAdd(int(num1), int(nthNumber))
            elif chooseBasicOperator == "-":
                result = basicCalculate.useSubtract(int(num1), int(nthNumber))
            elif chooseBasicOperator == "*":
                result = basicCalculate.useMultiply(int(num1), int(nthNumber))
            elif chooseBasicOperator == "/":
                result = basicCalculate.useDivide(int(num1), int(nthNumber))
            elif chooseBasicOperator == "**":
                result = basicCalculate.exponentialPow(int(num1), int(nthNumber))
            else:
                print("Invalid input")
            print(result)
            num1 = result

    elif basicOrAdvance == "advance":
        while True:
            if keyboard.is_pressed('esc'):
                print("Esc key pressed, exiting...")
                break
            chooseAdvanceOperator = input("Enter sin, cos, tan, cot, log, log10, log2, mod, exp, pi, e: ")
            nth_Number = float(input("Enter another number: "))

            result = 0

            if chooseAdvanceOperator == "sin":
                angleInRadians = math.radians(nth_Number)
                result = float(num1)*math.sin(float(angleInRadians))
            elif chooseAdvanceOperator == "cos":
                angleInRadians = math.radians(nth_Number)
                result = float(num1)*math.cos(float(angleInRadians))
            elif chooseAdvanceOperator == "tan":
                angleInRadians = math.radians(nth_Number)
                result = float(num1)*math.tan(float(angleInRadians))
            elif chooseAdvanceOperator == "cot":
                angleInRadians = math.radians(nth_Number)
                result = float(num1)*1/math.tan(float(angleInRadians))
            elif chooseAdvanceOperator == "log":
                base = float(input("Enter the base: "))
                result = float(num1)*math.log(nth_Number, base)
            elif chooseAdvanceOperator == "log10":
                result = float(num1)*math.log10(nth_Number)
            elif chooseAdvanceOperator == "log2":
                result = float(num1)*math.log2(nth_Number)
            elif chooseAdvanceOperator == "mod":
                result = float(num1)%nth_Number
            elif chooseAdvanceOperator == "exp":
                result = float(num1)*math.exp(nth_Number)
            elif chooseAdvanceOperator == "pi":
                result = float(num1)*math.pi
            elif chooseAdvanceOperator == "e":
                result = float(num1)*math.e
            else:
                print("Invalid operation or not implemented yet.")
            print(result)
            num1 = result
    else:
        print("Invalid input")

try:
    selectBasicOrAdvance(num1, basicOrAdvance)
except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("Program exited.")

