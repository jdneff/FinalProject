"""
Program: math_class.py
Author: Jonathan Neff
Last date modified: 10/27/2023

The purpose of this class to handle the math data
"""
import Queue

class MathClass:

    def __init__(self):
        self.math_queue = Queue()
        self.reset_the_game
        return

    def reset_the_game(self):
        """ sets up the game to the default/starting state"""
        for x in range (0, 9):
            for y in range (0, 9):
                problem = [x, y]
                self.math_queue.enqueue(problem)
        return

    def __str__(self):
        return "Row: " + str(self.label_row) + " Column: " + str(self.label_column)

    def __repr__(self):
         return "Row: " + str(self.label_row) + " Column: " + str(self.label_column)


