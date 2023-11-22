"""
Program: math_class.py
Author: Jonathan Neff
Last date modified: 11/22/2023

The purpose of this class to handle the math data
"""
import math_queue
import math_answers
import random

class MathClass:

    # constructor
    def __init__(self):
        # math queue to hold question to be answered
        self.math_queue = None
        # math queue to hold the questions and answer submitted
        self.math_answers = None
        # type of math being done
        self.math_operation = None
        # dictionary to translate math operations
        self.math_operations = { "Addition": "+",
                                 "Subtraction": "-",
                                 "Multiplication": "X",
                                 "Division": "/" }
        # storage for the current problem being asked
        self.current_problem = [];
        # number of questions to be asked before end of game
        self.number_of_questions = 0
        # questions asked so far in the game
        self.questions_asked = 0
        return

    # start the game, add problems into math queue
    def start_the_game(self, game_mode, number_of_questions):
        """ sets up the game to the default/starting state"""
        self.questions_asked = 0
        # build math_queue and math_answers objects
        self.math_queue = math_queue.MathQueue()
        self.math_answers = math_answers.MathAnswers()
        # save the chosen math operation
        self.math_operation = self.math_operations[game_mode]
        # save the number of questionst to be asked
        self.number_of_questions = number_of_questions

        # load problems into the math queue
        MAX_INT_ONE = 12
        MAX_INT_TWO = 12
        MULTIPLIER = 100
        for x in range (1, MAX_INT_ONE):
            for z in range (1, MAX_INT_TWO):
                y = x
                # exception for division so correct answers will be integers
                if (game_mode) == "Division":
                    y = y * z
                random_number = random.random() * MULTIPLIER
                problem = [y, z, random_number]
                self.math_queue.enqueue(problem)
        self.math_queue.randomize()
        return

    # get the next math problem from the math queue
    def get_problem(self):
        self.current_problem = self.math_queue.dequeue()
        return self.current_problem

    # submit the answer into the math answers priority que and return true/false
    def submit_answer(self, answer):
        self.questions_asked = self.questions_asked + 1
        is_correct = self.check_answer(self.current_problem[0], self.current_problem[1], self.math_operation, answer)
        correct_num = 0
        if is_correct:
            correct_num = 1
        self.math_answers.add(self.current_problem, answer, self.math_operation, correct_num)
        # return true/false
        return is_correct

    # determine if the user answer is correct or not
    def check_answer(self, num1, num2, operator, answer):
        if operator == "+":
            return num1 + num2 == answer
        elif operator == "-":
            return num1 - num2 == answer
        elif operator == "X":
            return num1 * num2 == answer
        elif operator == "/":
            return num1 / num2 == answer
        else:
            return False

    # retrieve the answers out of the queue
    def get_next_answer(self):
        return self.math_answers.remove()

    # output math class values in a string and return string
    def print_queue(self):
        output = ""
        output = output + self.math_operation + str(self.number_of_questions) + str(self.questions_asked)
        return output



