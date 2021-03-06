import fractions as f
import copy
from Program import print as p
# In this context an equation consists of the coefficients before each linear variable
# and a fraction that they sum up to
class Equation:

    # All new instances of Equation should be given a list of fractions upon creation
    # This constructor gets called when the program generates equations
    def __init__(self, x, denomlimit = 10000):
        self.lh_s = []
        for i in x:
            frac = f.Fraction(i).limit_denominator(denomlimit)
            self.lh_s.append(frac)
        self.lh_s_length = len(self.lh_s) - 1
        self.rh_s = self.lh_s.pop(len(self.lh_s)-1)

    def Zeroed(self):
        for koeff in self.lh_s:
            if koeff != 0:
                return False
        return True

    def DivideBySubstituteKoefficient(self, index):
        div = self.lh_s[index]
        for i in range(0, self.lh_s_length):
            self.lh_s[i] /= div
        self.rh_s /= div

    def ReduceBySubstitute(self, f, sub):
        for i in range(0, sub.lh_s_length):
            self.lh_s[i] -= f * sub.lh_s[i]
        self.rh_s -= f * sub.rh_s

    def DefinesXi(self):
        return self.lh_s.count(0) == self.lh_s_length - 1

    def GetLength(self):
        return self.lh_s_length
    def GetRhs(self):
        return self.rh_s

    def NonZeroValue(self):
        return self.index(not 0)



class EquationSystem:
    equations: []

    def __init__(self, equations):
        self.equations = equations

    def CheckForNoSolution(self):
        def Parallel(eq1, eq2, factor):
            for k in range(1, len(eq1.lh_s)):
                if not factor * eq2.lh_s[k] == eq1.lh_s[k]:
                    return False
            return True
        def FindFactor(lh_s1, lh_s2):
            for i in range(0, len(lh_s1)):
                if not lh_s2[i] == 0:
                    return lh_s1[i] / lh_s2[i]

        for i in range (0, 1 + int(len(self.equations)/2)):
            for j in range(0, 1 + int(len(self.equations)/2)):
                if i == j:
                    continue
                factor = FindFactor(self.equations[i].lh_s, self.equations[j].lh_s)
                if Parallel(self.equations[i], self.equations[j], factor):
                    if not (self.equations[i].rh_s / self.equations[j].rh_s == factor):
                        raise Exception("Solution doesn't exist")
                    raise Exception("Solution requires parameters")

    def Solve(self):
        # Copies initial values so that they can be displayed when the equation system is solved
        self.CheckForNoSolution()
        eqs = copy.deepcopy(self.equations)
        solvables = []
        while not self.SmallestReduction():
            solvables.append(self.Substitute())
        if not solvables[len(solvables)-1].DefinesXi():
            if len(solvables) < len(eqs):
                raise Exception("Solution doesn't exist")
            raise Exception("Solution requires parameters")
        solution = self.TurnIntoSolution(solvables)
        p.Print.print_sollution(eqs, solution)

    def TurnIntoSolution(self, solvs):
        # currently only gives a correct value for the final variable in the equation, needs a way to substitute
        # in solved variables in the following equations
        solution = []
        lan = solvs[0].lh_s_length
        for i in range(1, lan+1):
            if not solvs[lan-i].DefinesXi():
                EquationSystem.InputSolvedValues(solvs[lan-i], solution, lan-i)
            solution.append(solvs[lan-i].rh_s)
        return solution

    @staticmethod
    def InputSolvedValues(toBeSolved, solvedVariables, finalIndex):
        j = 0
        lan = toBeSolved.lh_s_length
        for i in range(1, lan - finalIndex):
            toBeSolved.rh_s -= toBeSolved.lh_s[lan-i] * solvedVariables[i-1]
            j += 1


    # Always goes from first to last variable, returns the equation that was used to substitute the system
    def Substitute(self):
        subst, index = self.FindSubstituteEquation()
        subst.DivideBySubstituteKoefficient(index)
        for i in range(0, len(self.equations)):
            fac = self.equations[i].lh_s[index]
            self.equations[i].ReduceBySubstitute(fac, subst)
        return subst

    def FindSubstituteEquation(self):
        # set to some high value so that the first equations first non zero coefficient becomes the initial candidate
        # for the "best" equation to substitute with (assuring that there will always be some equation that gives a
        # solution for the last variable)
        smallest_non_zero_index = 100
        # checks for the equation with the first non zeroed coefficient in lh_s
        for equation in self.equations:
            for i in range(0, len(self.equations[1].lh_s)):
                if equation.lh_s[i] != 0 and i < smallest_non_zero_index:
                    smallest_non_zero_index = i
                    smallest_non_zero = copy.deepcopy(equation)
                    break
        return smallest_non_zero, smallest_non_zero_index

    def SmallestReduction(self):
        for equation in self.equations:
            if not equation.Zeroed():
                return False
        return True
