class Print:
    @staticmethod
    def print_sollution(equations, sol):
        lan = len(sol)
        print("\nThe equation system:\n")
        for equation in equations:
            Print.formatized(equation.lh_s)
            print(f"  = {equation.rh_s}")
        print("\nHas the solution:\n")
        for i in range(0, lan):
            print(f"x{Print.__translate_index(i)} = {sol[lan-i-1]}")
    @staticmethod
    def formatized(expressions):
        for i in range(0, len(expressions)):
            Print.formatize(expressions[i], i)
        return

    @staticmethod
    def formatize(exp, i):
        sep = "+" if exp >= 0 else "-"
        if i == 0:
            if exp == 0:
                return

            if exp == 1:
                print(f"x" + Print.__translate_index(i), end="")
                return

            if exp < 0:
                print(f"{sep}{-1*exp}x" + Print.__translate_index(i), end="")

            if exp > 0:
                print(f"{exp}x" + Print.__translate_index(i), end="")
            return


        if exp == 0:
            return

        if abs(exp) == 1:
            print(f" {sep} x" + Print.__translate_index(i), end="")
            return

        if exp < 0:
            print(f" {sep} {-1 * exp}x" + Print.__translate_index(i), end="")

        if exp > 0:
            print(f" {sep} {exp}x" + Print.__translate_index(i), end="")

        return
    @staticmethod
    def __translate_index(i):
        trs = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        index = f"{i}"
        return index.translate(trs)
