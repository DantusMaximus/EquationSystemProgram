from Program import file_reader as file
from Program import equation_system_generator_app as eq
import os
class UserInput:
    @staticmethod
    def read():
        inp = int(input("Do you wish for the program to solve a specified[0] or generated[1] equation system? [0/1]"))
        if inp == 0:
            return file.FileReader.read("EquationSystem.txt")
        if inp == 1:
            os.system('cls')
            spec = input("How many variables?")
            return eq.Generate
