"""
Program: math_answers.py
Author: Jonathan Neff
Last date modified: 11/3/2023

The purpose of this class is to store the math answers submitted
This class is a priority queue
"""
class PriorityQueueItem:

    def __init__(self, problem, answer, operation, is_correct ):
        self.problem = problem
        self.operation = operation
        self.answer = answer
        self.is_correct = is_correct

class MathAnswers:

    def __init__(self):
        self.items = [];

    def is_empty(self):
       return len(self.items) == 0;

    def add(self, problem, answer, operation, is_correct):
        newItem = PriorityQueueItem(problem, answer, operation, is_correct)
        if self.is_empty():
            self.items.append(newItem)
        else:
            for x in range(len(self.items)):
                item = self.items[x]
                if newItem.is_correct > item.is_correct:
                    # insert in order
                    self.items.insert(x, newItem)
                    return
            # add at the end
            self.items.insert(x, newItem)

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
