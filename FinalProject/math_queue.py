"""
Program: math_queue.py
Author: Jonathan Neff
Last date modified: 11/17/2023

The purpose of this class is to manage the math problems that will be asked
"""

import QueueEmptyException

class MathQueue:
    def __init__(self):
        self._items = [];

    def is_empty(self):
       return len(self._items) == 0;

    def is_full(self):
        # linked based queue is never full
        return False

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
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

    def randomize(self):
        self.customSort()
        return

    def customSort(self):
        x = 0
        y = x + 1
        SORT_IDX = 2
        while (x < self.size() - 1):
            item1 = self._items[x]
            item2 = self._items[y]
            if item1[SORT_IDX] > item2[SORT_IDX]:
                self._items[x] = item2
                self._items[y] = item1
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
        if self.is_empty():
            raise QueueEmptyException.QueueEmptyException
        else:
            stack_str = ""
            for item in self._items:
                stack_str = stack_str + str(item) + "\n"
            return stack_str;
