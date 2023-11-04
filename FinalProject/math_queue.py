"""
Program: math_queue.py
Author: Jonathan Neff
Last date modified: 11/3/2023

The purpose of this class is to manage the math problems that will be asked
"""

import QueueEmptyException

class MathQueue:
    def __init__(self):
        self.items = [];

    def is_empty(self):
       return len(self.items) == 0;

    def is_full(self):
        # linked based queue is never full
        return false

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
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

    def randomize(self):
        self.customSort()
        return


    def customSort(self):
        x = 0
        y = x + 1
        SORT_IDX = 2
        while (x < self.size() - 1):
            item1 = self.items[x]
            item2 = self.items[y]
            if item1[SORT_IDX] > item2[SORT_IDX]:
                self.items[x] = item2
                self.items[y] = item1
                if x > 0:
                    x -= 1
                    y -= 1
                else:
                    x += 1
                    y += 1
            else:
                x += 1
                y += 1
        return

    def print_queue(self):
        if self.is_empty:
            raise QueueEmptyException
        else:
            stack_str = ""
            for itme in self.items:
                stack_str += item + "\n"
            return stack_str;
