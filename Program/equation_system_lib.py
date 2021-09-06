import fractions as f
from Program import print as p
# In this context an equation consists of the coefficients before each linear variable
# and a fraction that they sum up to
class Equation:

    # All new instances of Equation should be given a list of fractions upon creation
    def __init__(self, x):
        self.lh_s = [f.Fraction]
        for i in x:
            frac = f.Fraction(int(i), 1)
            self.lh_s.append(frac)
        self.lh_s_length = len(self.lh_s) - 2
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
    def DefinesXi(self):
        return self.lh_s.count() == self.lh_s_length - 1
    def GetLength(self):
        return self.lh_s_length



class EquationSystem:
    equations: [Equation]

    def __init__(self, equations):
        self.equations = equations

    def Solve(self):
        # A list of equations with 1, 2, 3 etc (possibly with a lowest value higher than 1 so that the solution
        # is written in terms of some parameters) so that the program can solve for some list of variables xi
        solvables = [EquationSystem]
        sollution = [f.Fraction] * self.equations[1].GetLength()
        while not self.equations.SmallestReduction():
            solvables.append(self.equations.Substitute())
        if(solvables[len(solvables)-1].DefinesXi()):
            raise NotImplemented
        next_x = int
        for i in range(len(solvables)-1, 0):
            if(solvables[i].DefinesXi()):
                sollution.append(i)
                continue
            next_x -= solvables[i].rh_s
            for xi in sollution:
                next_x -= xi
            sollution[i] = next_x
        p.Print.print_sollution(sollution)

    # Always goes from first to last variable, returns the equation that was used to substitute the system
    def Substitute(self):
        subst, index = self.FindSubstituteEquation()
        subst.DivideBySubstituteKoefficient(index)
        for i in range(0, len(self.equations) -1):
            fac = self.equations[index]
            self.equations[index].ReduceBySubstitute(fac, subst)
        return subst

    def FindSubstituteEquation(self):
        smallest_non_zero = Equation
        smallest_non_zero_index = 100
        for equation in self.equations:
            for i in range(0, len(equation) - 1):
                if equation[i] == 0 and i < smallest_non_zero_index:
                    smallest_non_zero = equation
                    smallest_non_zero_index = i
                    break
        return smallest_non_zero, smallest_non_zero_index


    def SmallestReduction(self):
        val = self.equations[0]  # initializes, the actual value is nonsense
        for equation in self.equations:
            if equation == val or equation.Zeroed():
                continue
            if equation != val or equation.Zeroed():
                return False
        return True
