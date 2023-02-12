class Queue2Stacks(object):
    """
    While stack1 is not empty, push everything from stack1 to stack2.
    Push x to stack1 (assuming size of stacks is unlimited).
    Push everything back to stack1.

    Time Complexity:  O(n).\n
    Space Complexity: O(n).
    """
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def enqueue(self, item):
        while len(self.inStack) != 0:
            self.outStack.append(self.inStack[-1])
            self.inStack.pop()

        self.inStack.append(item)

        while len(self.outStack) != 0:
            self.inStack.append(self.outStack[-1])
            self.outStack.pop()

    def dequeue(self):
        return self.inStack.pop()


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
        self.inStack = []
        self.outStack = []

    def enqueue(self, item):
        self.inStack.append(item)

    def dequeue(self):
        if len(self.outStack) == 0 and len(self.inStack) > 0:
            while len(self.inStack) != 0:
                self.outStack.append(self.inStack.pop())
            return self.outStack.pop()

        else:
            return self.outStack.pop()


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
