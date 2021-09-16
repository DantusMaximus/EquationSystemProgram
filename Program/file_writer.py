from Program import equation_system_lib as e


class FileWriter:
    @staticmethod
    def write(file_name, eq):
        file = open(file_name, "w")
        for equation in eq:
            for v in equation.lh_s:
                file.write(f"{v} ")
            file.write(f"{equation.rh_s}\n")
