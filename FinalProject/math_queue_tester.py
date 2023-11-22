"""
math_queue_tester.py
Author: Jonathan Neff
Last date modified: 11/22/2023

The purpose of this class is to test the MathQueue Class
"""

import QueueEmptyException
import unittest
import math_queue as mq


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.math_queue = mq.MathQueue()

    def tearDown(self):
        del self.math_queue

    def test_mathQueueExceptions(self):

        # test peek() before adding anything
        self.assertRaises(QueueEmptyException.QueueEmptyException, self.math_queue.peek)

        # test empty dequeue
        self.assertRaises(QueueEmptyException.QueueEmptyException, self.math_queue.dequeue)

        #test empty print
        self.assertRaises(QueueEmptyException.QueueEmptyException, self.math_queue.print_queue)

    def test_mathQueue(self):

        problem1 = [1, 2, 5]
        problem2 = [2, 2, 4]
        problem3 = [5, 5, 1]
        # test enqueue
        self.math_queue.enqueue(problem1)
        self.math_queue.enqueue(problem2)
        self.math_queue.enqueue(problem3)
        self.math_queue.randomize()

        # test peek
        self.assertEqual(self.math_queue.peek(), [5, 5, 1])

        # test size
        self.assertEqual(self.math_queue.size(), 3)

        # test dequeue (and randomize and customsort)
        removedItem = self.math_queue.dequeue()
        self.assertEqual(removedItem, [5, 5, 1])
        self.assertEqual(self.math_queue.size(), 2)

        # test is_full()
        self.assertEqual(self.math_queue.is_full(), False)

        # test is_empty()
        self.assertEqual(self.math_queue.is_empty(), False)

        # test print_queue
        self.assertEqual(self.math_queue.print_queue(), "[2, 2, 4]\n[1, 2, 5]\n")

if __name__ == '__main__':
    unittest.main()

