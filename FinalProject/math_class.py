"""
Program: math_class.py
Author: Jonathan Neff
Last date modified: 10/27/2023

The purpose of this class to handle the math data
"""
import math_queue
import math_answers
import random

class MathClass:

    def __init__(self):
        self.math_queue = math_queue.MathQueue()
        self.math_operation = "+"
        self.current_problem = [];
        self.reset_the_game
        return

    def reset_the_game(self):
        """ sets up the game to the default/starting state"""
        MULTIPLIER = 100
        for x in range (0, 9):
            for y in range (0, 9):
                random_number = random.random() * MULTIPLIER
                problem = [x, y, random_number]
                self.math_queue.enqueue(problem)
        self.math_queue.randomize()
        return

    def get_problem(self):
        self.current_problem = math_queue.dequeue()
        return self.current_problem

    def submit_answer(self, answer):
        math_answers.add(self.current_problem, answer, self.math_operation)

    def __str__(self):
        return "Row: " + str(self.label_row) + " Column: " + str(self.label_column)

    def __repr__(self):
         return "Row: " + str(self.label_row) + " Column: " + str(self.label_column)


