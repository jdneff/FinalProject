"""
Program: math_answers.py
Author: Jonathan Neff
Last date modified: 11/17/2023

The purpose of this class is to store the math answers submitted
This class is a priority queue
"""

import QueueEmptyException

class PriorityQueueItem:

    def __init__(self, problem, answer, operation, is_correct ):
        self._problem = problem
        self._operation = operation
        self._answer = answer
        self._is_correct = is_correct

class MathAnswers:

    def __init__(self):
        self._items = [];

    def is_empty(self):
       return len(self._items) == 0;

    def is_full(self):
        return False

    def add(self, problem, answer, operation, is_correct):
        newItem = PriorityQueueItem(problem, answer, operation, is_correct)
        if self.is_empty():
            self._items.append(newItem)
        else:
            for x in range(len(self._items)):
                item = self._items[x]
                if newItem._is_correct > item._is_correct:
                    # insert in order
                    self._items.insert(x, newItem)
                    return
            # add at the end
            self._items.append(newItem)

    def remove(self):
        if self.is_empty():
            raise QueueEmptyException.QueueEmptyException("The math queue is empty")
        else:
            return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            raise QueueEmptyException.QueueEmptyException("The math queue is empty")
        else:
            return self._items[0]

    def size(self):
        return len(self._items)

    def print_queue(self):
        if self.is_empty():
            raise QueueEmptyException.QueueEmptyException("The math queue is empty")
        else:
            stack_str = ""
            for item in self._items:
                stack_str += str(item._problem) + "\n"
            return stack_str;
