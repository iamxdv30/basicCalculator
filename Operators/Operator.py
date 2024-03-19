import math

class Operator:

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