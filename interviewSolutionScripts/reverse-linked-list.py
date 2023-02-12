class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, newData):
        if self.head is None:
            self.head = Node(newData)

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            newNode = Node(newData)
            temp.next = newNode

    def printList(self):
        temp = self.head

        while temp:
            print(temp.value, end=" ")
            temp = temp.next

    def reverse(self):
        currNode = self.head
        prevNode = None

        while currNode.next is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        currNode.next = prevNode

        return currNode


llist = LinkedList()
llist.append(20)
llist.append(4)
llist.append(15)
llist.append(10)
llist.append(30)

print(llist.printList())
reverse = llist.reverse()

while reverse:
    print(reverse.value, end=" ")
    reverse = reverse.next
