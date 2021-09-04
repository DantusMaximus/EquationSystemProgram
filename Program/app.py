from Program import equation_system_lib as eLib
from Program import file_reader as file
import fractions as f
from Program import user_input as u
# returns an equation system based upon what the user's input
eq = u.UserInput.read()
eq.Solve()
print(f.Fraction(2, 3))
# we need each equation to in the form of a list of values matching with the corresponding coefficient to the
# indexed variable.
