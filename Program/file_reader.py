from Program import equation_system_lib as e


class FileReader:
    @staticmethod
    def read(file_name):
        file = open(file_name, "r")
        str_lines = file.readlines()
        equations = [e.Equation]
        for str_line in str_lines:
            line = str_line.replace('\n', "")
            line = line.split(" ")
            equation = e.Equation(line)
            equations.append(equation)
        return e.EquationSystem(equations)
