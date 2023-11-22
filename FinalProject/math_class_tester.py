"""
math_class_tester.py
Author: Jonathan Neff
Last date modified: 11/22/2023

The purpose of this class is to test the MathClass Class
"""

import unittest
import math_class as mc


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.math_class = mc.MathClass()

    def tearDown(self):
        del self.math_class

    def test_mathQueue(self):

        # test start_game and get_problem
        self.math_class.start_the_game("Addition", 10)
        problem = self.math_class.get_problem()
        self.assertIsInstance(problem, list)

        # test submit answer and check_answer
        answer = problem[0] + problem[1]
        self.assertEqual(self.math_class.submit_answer(answer), True)

        # test get_next_answer
        answer = problem[0] + problem[1]
        self.assertEqual(self.math_class.get_next_answer().answer, answer)


        # test print_queue
        self.assertEqual(self.math_class.print_queue(), "+101")

if __name__ == '__main__':
    unittest.main()
