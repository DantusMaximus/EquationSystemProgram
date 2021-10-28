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
        firstNonZero = True
        for i in range(0, len(expressions)):
            Print.formatize(expressions[i], i, firstNonZero)
            if expressions[i] != 0:
                firstNonZero = False
        return
    @staticmethod
    def formatize(exp, i, firstNonZero):
        sep = "+" if exp >= 0 else "-"
        if firstNonZero and exp > 0:
            sep = ""
        if i == 0:
            if exp == 0:
                return

            if exp == 1:
                Print.printline(f"x", i)
                return

            if exp < 0:
                Print.printline(f"{sep}{-1*exp}x", i)

            if exp > 0:
                Print.printline(f"{exp}x", i)
            return


        if exp == 0:
            return

        if abs(exp) == 1:
            Print.printline(f" {sep} x", i)
            return

        if exp < 0:
            Print.printline(f" {sep} {-1 * exp}x", i)

        if exp > 0:
            Print.printline(f" {sep} {exp}x", i)


        return
    @staticmethod
    def __translate_index(i):
        trs = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        index = f"{i}"
        return index.translate(trs)

    @staticmethod
    def printline(text, i):
        print(text + Print.__translate_index(i), end="")