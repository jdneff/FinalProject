"""
math_queue_answers_tester.py
Author: Jonathan Neff
Last date modified: 11/17/2023

The purpose of this class is to test the MathAnswers Class
"""

import QueueEmptyException
import unittest
import math_answers as ma


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.math_answers = ma.MathAnswers()

    def tearDown(self):
        del self.math_answers

    def test_mathQueueExceptions(self):

        # test peek() before adding anything
        self.assertRaises(QueueEmptyException.QueueEmptyException, self.math_answers.peek)

        # test empty remove
        self.assertRaises(QueueEmptyException.QueueEmptyException, self.math_answers.remove)

        #test empty print
        self.assertRaises(QueueEmptyException.QueueEmptyException, self.math_answers.print_queue)

    def test_mathAnswers(self):

        problem1 = [1, 2, 5]
        problem2 = [2, 2, 4]
        problem3 = [5, 5, 1]
        answer1 = 3
        answer2 = 4
        answer3 = 77
        operation = "+"
        is_correct_1 = 1
        is_correct_2 = 1
        is_correct_3 = 0

        # test add
        self.math_answers.add(problem1, answer1, operation, is_correct_1)
        self.math_answers.add(problem2, answer2, operation, is_correct_2)
        self.math_answers.add(problem3, answer3, operation, is_correct_3)

        # test peek
        self.assertEqual(self.math_answers.peek()._problem, [1, 2, 5])

        # test size
        self.assertEqual(self.math_answers.size(), 3)

        # test remove
        removedItem = self.math_answers.remove()._problem
        self.assertEqual(removedItem, [1, 2, 5])
        self.assertEqual(self.math_answers.size(), 2)

        # test is_full()
        self.assertEqual(self.math_answers.is_full(), False)

        # test is_empty()
        self.assertEqual(self.math_answers.is_empty(), False)

        # test print_queue
        self.assertEqual(self.math_answers.print_queue(), "[2, 2, 4]\n[5, 5, 1]\n")

if __name__ == '__main__':
    unittest.main()
