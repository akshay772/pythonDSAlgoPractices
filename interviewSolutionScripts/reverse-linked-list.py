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
        """
        The idea is to use three pointers curr, prev, and next to keep track of nodes to update reverse links.\n

        Time Complexity: O(N), Traversing over the linked list of size N.\n
        Auxiliary Space: O(1) \n

        :return:
        """
        currNode = self.head
        prevNode = None

        while currNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        self.head = prevNode

    def reverseRecursion(self, head):
        """
        The idea is to reach the last node of the linked list using recursion then start reversing the linked list.\n
        Divide the list in two parts – first node and rest of the linked list.
        Call reverse for the rest of the linked list.
        Link the rest linked list to first.
        Fix head pointer to NULL

        Time Complexity: O(N), Visiting over every node one time \n
        Auxiliary Space: O(N), Function call stack space \n

        :return:
        """
        if head is None or head.next is None:
            return head

        rest = self.reverseRecursion(head.next)

        head.next.next = head
        head.next = None

        return rest

    def reverseUtil(self, currNode, prev):
        if currNode.next is None:
            self.head = currNode
            currNode.next = prev
            return

        nextNode = currNode.next
        currNode.next = prev

        self.reverseUtil(nextNode, currNode)

    def reverseRecursionTail(self):
        """
        The idea is to maintain three pointers previous, current and next, recursively visit every node and make
        links using these three pointers.\n
        First update next with next node of current i.e. next = current->next
        Now make a reverse link from current node to previous node i.e. curr->next = prev
        If the visited node is the last node then just make a reverse link from the current node to previous node and
        update head.

        Time Complexity: O(N), Visiting every node of the linked list of size N.
        Auxiliary Space: O(N), Function call stack space

        :return:
        """
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def reverseStack(self, head):
        """
        The idea is to store the all the nodes in the stack then make a reverse linked list.\n
        Store the nodes(values and address) in the stack until all the values are entered.
        Once all entries are done, Update the Head pointer to the last location(i.e. the last value).
        Start popping the nodes(value and address) and store them in the same order until the stack is empty.
        Update the next pointer of last Node in the stack by NULL.\n

        Time Complexity: O(N), Visiting every node of the linked list of size N.
        Auxiliary Space: O(N), Space is used to store the nodes in the stack.

        :param head:
        :return:
        """
        stack, temp = [], head

        while temp:
            stack.append(temp)
            temp = temp.next

        head = temp = stack.pop()

        while len(stack) > 0:
            temp.next = stack.pop()
            temp = temp.next

        temp.next = None
        return head


llist = LinkedList()
llist.append(20)
llist.append(4)
llist.append(15)
llist.append(10)
llist.append(30)

llist.printList()
print("------->")
llist.reverse()
llist.printList()

print("\n")
llist.printList()
print("------->")
llist.head = llist.reverseRecursion(llist.head)
llist.printList()

print("\n")
llist.printList()
print("------->")
llist.head = llist.reverseStack(llist.head)
llist.printList()
