class Queue2Stacks(object):
    """
    While stack1 is not empty, push everything from stack1 to stack2.
    Push x to stack1 (assuming size of stacks is unlimited).
    Push everything back to stack1.

    Time Complexity:  O(n).\n
    Space Complexity: O(n).
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        self.stack1.append(item)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def dequeue(self):
        return self.stack1.pop()


class Queue2StacksMoveOnce(object):
    """
    enQueue(q,  x)
        Push x to stack1 (assuming size of stacks is unlimited). Here time complexity will be O(1)
    deQueue(q)
        f both stacks are empty then error.
        If stack2 is empty
        While stack1 is not empty, push everything from stack1 to stack2.
        Pop the element from stack2 and return it.

    Time Complexity: Push operation: O(1). Same as pop operation in stack. Pop operation: O(N) in general and O(
    1)amortized time complexity. In the worst case we have to empty the whole of stack 1 into stack 2 so its O(N).
    Amortized time is the way to express the time complexity when an algorithm has the very bad time complexity only
    once in a while besides the time complexity that happens most of time. So its O(1) amortized time complexity,
    since we have to empty whole of stack 1 only when stack 2 is empty, rest of the times the pop operation takes O(
    1) time.\n
    Auxiliary Space: O(N). Use of stack for storing values.
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack2) == 0 and len(self.stack1) > 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

        else:
            return self.stack2.pop()


class Queue2StacksRecursive(object):
    def __init__(self):
        self.stack = []

    def enqueue(self, item):
        self.stack.append(item)

    def dequeue(self):
        if len(self.stack) == 0:
            return

        top = self.stack[len(self.stack) - 1]
        self.stack.pop()

        if len(self.stack) == 0:
            return top

        item = self.dequeue()
        self.stack.append(top)

        return item


q = Queue2StacksRecursive()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
