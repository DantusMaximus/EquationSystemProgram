from Program import file_reader as file
from Program import equation_system_generator_app as eq
import os
class UserInput:
    @staticmethod
    def read():
        while True:
            inp = int(input("Do you wish for the program to solve a specified[0] or generated[1] equation system? [0/1]"))
            if inp == 0:
                return file.FileReader.read("EquationSystem.txt")
            if inp == 1:
                while True:
                    varCount = int(input("How many variables?"))
                    if varCount <= 1: continue
                    while True:
                        denomLim = int(input("What should the maximum value in any denominator be for said equation system?"))
                        if denomLim < 1: continue
                        return eq.EquationSystemGenerator.Generate(varCount, denomLim)
