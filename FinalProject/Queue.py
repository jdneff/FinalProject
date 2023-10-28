class Queue:
    def __init__(self, max_size=5):
        self.items = [];

    def is_empty(self):
       return items.Count == 0;

    def is_full(self):
        # linked based queue is never full
        return false

    def enqueue(self, item):
       items.append(item)

    def dequeue(self):
        if this.isEmpty:
            raise QueueEmptyException
        else:
            return items.remove()

    def peek(self):
        if this.isEmpty:
            raise QueueEmptyException
        else:
            return items[0]

    def size(self):
        return items.Count

    def print_queue(self):
        if this.isEmpty:
            raise QueueEmptyException
        else:
            stack_str = ""
            for itme in items:
                stack_str += item + "\n"
            return stack_str;
