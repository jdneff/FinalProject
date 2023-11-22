"""
Program: math_answers.py
Author: Jonathan Neff
Last date modified: 11/22/2023

The purpose of this class is to store the math answers submitted
This class is a priority queue
"""

import QueueEmptyException

class PriorityQueueItem:

    def __init__(self, problem, answer, operation, is_correct ):
        self.problem = problem
        self.operation = operation
        self.answer = answer
        self.is_correct = is_correct

class MathAnswers:

    def __init__(self):
        self._items = [];

    # check if empty
    def is_empty(self):
       return len(self._items) == 0;

    # never full
    def is_full(self):
        return False

    # add a new item to the priority queue
    def add(self, problem, answer, operation, is_correct):
        newItem = PriorityQueueItem(problem, answer, operation, is_correct)
        if self.is_empty():
            self._items.append(newItem)
        else:
            for x in range(len(self._items)):
                item = self._items[x]
                if newItem.is_correct > item.is_correct:
                    # insert in order
                    self._items.insert(x, newItem)
                    return
            # add at the end
            self._items.append(newItem)

    # remove and return an item from the queue
    def remove(self):
        if self.is_empty():
            raise QueueEmptyException.QueueEmptyException("The math queue is empty")
        else:
            return self._items.pop(0)

    # return but dont remove the next item in the queue
    def peek(self):
        if self.is_empty():
            raise QueueEmptyException.QueueEmptyException("The math queue is empty")
        else:
            return self._items[0]

    # return the current size of the priority queue
    def size(self):
        return len(self._items)

    # return a string with items in the priority queue
    def print_queue(self):
        if self.is_empty():
            raise QueueEmptyException.QueueEmptyException("The math queue is empty")
        else:
            stack_str = ""
            for item in self._items:
                stack_str += str(item.problem) + "\n"
            return stack_str;
