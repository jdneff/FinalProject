"""
Program: math_answers.py
Author: Jonathan Neff
Last date modified: 11/3/2023

The purpose of this class is to store the math answers submitted
This class is a priority queue
"""
class PriorityQueueItem:

    def __init__(self, problem, answer ):
        self.problem = problem
        self.answer = answer
        #if problem[0] ? problem[1] == answer:
        #   self.correct = 1
        #else:
        #    self.correct = 0

class MathAnswers:

    def __init__(self):
        self.items = [];

    def is_empty(self):
       return len(self.items) == 0;

    def is_full(self):
        # linked based queue is never full
        return false

    def add(self, problem, answer, operation):
        newItem = PriorityQueueItem(problem, answer)
        if self.items.is_empty():
            self.items.append(item)
        else:
            return
            #compareNode = self.items[0]
            #while newItem.

    def remove(self):
        if self.is_empty():
            raise QueueEmptyException.QueueEmptyException("The math queue is empty")
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty:
            raise QueueEmptyException
        else:
            return self.items[0]

    def size(self):
        return len(self.items)

    def print_queue(self):
        if self.is_empty:
            raise QueueEmptyException
        else:
            stack_str = ""
            for itme in self.items:
                stack_str += item + "\n"
            return stack_str;
