

class basicOperator:
    def __init__(self):
        pass

    def useAdd(self, *args):
        return sum(args)
    def useSubtract(self, *args):
        return args[0] - args[1]
    def useMultiply(self, *args):
        return args[0] * args[1]
    def useDivide(self, *args):
        return args[0] / args[1]
    def exponentialPow(self, *args):
        return args[0] ** args[1]

# The basicOperator class contains the add, subtract, multiply, divide, and power methods.