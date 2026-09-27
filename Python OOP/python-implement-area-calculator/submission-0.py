import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *parameter):
        if len(parameter) == 1:
            return round(math.pi * parameter[0] ** 2, 2)
        else:
            return parameter[0] * parameter[1]
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
