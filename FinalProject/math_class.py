"""
Program: math_class.py
Author: Jonathan Neff
Last date modified: 11/10/2023

The purpose of this class to handle the math data
"""
import math_queue
import math_answers
import random

class MathClass:

    def __init__(self):
        # math queue to hold question to be answered
        self._math_queue = None
        # math queue to hold the questions and answer submitted
        self._math_answers = None
        # type of math being done
        self._math_operation = None
        # dictionary to translate math operations
        self._math_operations = { "Addition": "+",
                                 "Subtraction": "-",
                                 "Multiplication": "X",
                                 "Division": "/" }
        # storage for the current problem being asked
        self._current_problem = [];
        # number of questions to be asked before end of game
        self._number_of_questions = 0
        # questions asked so far in the game
        self._questions_asked = 0
        return

    def start_the_game(self, game_mode, number_of_questions):
        """ sets up the game to the default/starting state"""
        self._questions_asked = 0
        # build math_queue and math_answers objects
        self._math_queue = math_queue.MathQueue()
        self._math_answers = math_answers.MathAnswers()
        # save the chosen math operation
        self._math_operation = self._math_operations[game_mode]
        # save the number of questionst to be asked
        self._number_of_questions = number_of_questions

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
                self._math_queue.enqueue(problem)
        self._math_queue.randomize()
        return

    # get the next math problem from the math queue
    def get_problem(self):
        self._current_problem = self._math_queue.dequeue()
        return self._current_problem

    # submit the answer into the math answers priority que and return true/false
    def submit_answer(self, answer):
        self._questions_asked = self._questions_asked + 1
        is_correct = self.check_answer(self._current_problem[0], self._current_problem[1], self._math_operation, answer)
        correct_num = 0
        if is_correct:
            correct_num = 1
        self._math_answers.add(self._current_problem, answer, self._math_operation, correct_num)
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
        return self._math_answers.remove()

    def print_queue(self):
        output = ""
        output = output + self._math_operation + str(self._number_of_questions) + str(self._questions_asked)
        return output



