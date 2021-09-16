from Program import equation_system_lib as e
from Program import file_writer as w
import random
class EquationSystemGenerator:
    @staticmethod
    def Generate(varCount, denomLim):
        colrowCount = varCount + 1
        equations = []
        for r in range(0, colrowCount - 1):
            equation = e.Equation
            lst = []
            for c in range(0, colrowCount):
                #50% chance to be positive/negative
                if(random.random() <= 0.4):
                    lst.append(random.uniform(10, 100))
                    continue
                lst.append(-1*random.uniform(10, 100))
            equation = e.Equation(lst, denomLim)
            equations.append(equation)
        w.FileWriter.write("GeneratedEquationSystem.txt", equations)
        return e.EquationSystem(equations)
