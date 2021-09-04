import fractions as f

# In this context an equation consists of the coefficients before each linear variable
# and a fraction that they sum up to
class Equation:

    # All new instances of Equation should be given a list of fractions upon creation
    def __init__(self, x):
        self.lh_s: []
        for i in x:
            frac = f.Fraction(int(i), 1)
            self.lh_s.append(frac)
        self.len = len(self.lh_s)
        self.rh_s = self.lh_s.pop(len(self.lh_s)-1)
        print(self.rh_s)
    def Zeroed(self):
        for koeff in self.lh_s:
            if koeff != 0:
                return False
        return True
    def DivideBySubstituteKoefficient(self, index):
        div = self.lh_s[index]
        for i in range(0, self.lh_s) - 1:
            self.lh_s[i] /= div
        self.rh_s /= div
    def ReduceBySubstitute(self, f, sub):
        for i in range(0, self.len - 1):
            self.lh_s[i] -= f * sub[i]
        self.rh_s -= f * sub.rh_s




class EquationSystem:
    equations: [Equation]

    def __init__(self, equations):
        self.equations = equations

    def Solve(self):
        # A list of equations with 1, 2, 3 etc (possibly with a lowest value higher than 1 so that the solution
        # is written in terms of some parameters) so that the program can solve for some list of variables xi
        solvables = EquationSystem[len(self.equations)]
        while not self.equations.SmallestReduction():
            solvables.append(self.equations.Substitute())

    # Always goes from first to last variable, returns the equation that was used to substitute the system
    def Substitute(self):
        subst, index = self.FindSubstituteEquation()
        subst.DivideBySubstituteKoefficient(index)
        for i in range(0, len(self.equations) -1):
            fac = self.equations[index]
            self.equations[index].ReduceBySubstitute(fac, subst)

    def FindSubstituteEquation(self):
        smallest_non_zero: Equation
        smallest_non_zero_index = 100
        for equation in self.equations:
            for i in range(0, len(equation) - 1):
                if equation[i] == 0 and i < smallest_non_zero_index:
                    smallest_non_zero = equation
                    smallest_non_zero_index = i
                    break
        return smallest_non_zero, smallest_non_zero_index


    def SmallestReduction(self):
        val = self.equations[0]
        for equation in self.equations:
            if equation == val or equation.Zeroed():
                continue
