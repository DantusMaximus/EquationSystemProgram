from Program import equation_system_lib as e
import random
class EquationSystemGenerator:
    @staticmethod
    def Generate(varCount):
        colrowCount = int(varCount)+1
        equations = []
        for r in range(0, colrowCount):
            equation = e.Equation
            lst = []
            for c in range(0, colrowCount):
                lst.append(random.uniform(0, 10))
            equation
            equations.append(equation)
        return e.EquationSystem(equations)
