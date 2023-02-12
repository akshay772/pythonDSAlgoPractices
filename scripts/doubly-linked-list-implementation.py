class DoublyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.prevNode = None
        self.nextNode = None


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.nextNode = b
b.prevNode = a

b.nextNode = c
c.prevNode = b
