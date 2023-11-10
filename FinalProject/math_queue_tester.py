"""
math_queue_tester.py
Author: Jonathan Neff
Last date modified: 11/10/2023

The purpose of this class is to test the MathQueue Class
"""

import unittest
import math_queue as mq


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.math_queue = mq.MathQueue()

    def tearDown(self):
        del self.math_queue

    def test_something(self):
        problem = [1, 2, 5]
        self.math_queue.enqueue(problem)
        self.assertEqual(self.math_queue.size(), 1)
        self.math_queue.enqueue(problem)
        self.assertEqual(self.math_queue.size(), 2)

if __name__ == '__main__':
    unittest.main()

