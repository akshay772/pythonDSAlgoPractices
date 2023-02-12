class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newData):
        newNode = Node(newData)
        newNode.nextNode = self.head
        self.head = newNode

    def printList(self):
        temp = self.head

        while temp:
            print(temp.value, end=" ")
            temp = temp.nextNode

    def detectLoop(self):
        """
        The idea is to insert the nodes in the hashmap and whenever a node is encountered that is already present in
        the hashmap then return true.\n

        Time complexity: O(N), Only one traversal of the loop is needed.\n
    Auxiliary Space: O(N), N is the space required to store the value in the hashmap.

        :return:
        """
        hashMap = set()
        temp = self.head

        while temp:
            if temp in hashMap:
                return True

            hashMap.add(temp)
            temp = temp.nextNode

        return False


class NodeFlag(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.flag = 0


def push(headNode, newData):
    newNode = NodeFlag(newData)
    newNode.flag = 0

    newNode.next = headNode
    headNode = newNode

    return headNode


def printList(headNode):
    temp = headNode

    while temp:
        print(temp.value, end=" ==> ")
        temp = temp.next


def detectLoop(headNode):
    """
    The idea is to modify the node structure by adding flag in it and mark the flag whenever visit the node.\n

    Time complexity: O(N), Only one traversal of the loop is needed.\n
    Auxiliary Space: O(1)\n

    :param headNode:
    :return:
    """
    while headNode is not None:
        if headNode.flag == 1:
            return True

        headNode.flag = 1
        headNode = headNode.next

    return False


def detectLoopSlowFast(headNode):
    """
    This algorithm is used to find a loop in a linked list. It uses two pointers one moving twice as fast as the
    other one. The faster one is called the faster pointer and the other one is called the slow pointer.\n

    Time complexity: O(N), Only one traversal of the loop is needed.\n
    Auxiliary Space: O(1). \n

    :param headNode:
    :return:
    """
    slowPtr = headNode
    fastPtr = headNode

    while slowPtr and fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

        if slowPtr == fastPtr:
            return True

    return False


def detectLoopMarkingVisited(headNode):
    """
    The idea is to point the current node of the linked list to a node which is created. Whenever a node’s next is
    pointing to that node it means loop is there.

    Time complexity: O(N), Only one traversal of the loop is needed.\n
    Auxiliary Space: O(1). \n

    :param headNode:
    :return:
    """
    temp = ''

    while headNode is not None:
        if headNode.next is None:
            return False

        if headNode.next == temp:
            return True

        nextNode = headNode.next
        headNode.next = temp
        headNode = nextNode

    return False


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

llist.head.nextNode.nextNode.nextNode = llist.head

if llist.detectLoop():
    print('Loop Found')
else:
    print('No Loop')

head = None
head = push(head, 20)
head = push(head, 4)
head = push(head, 15)
head = push(head, 10)

head.next.next.next.next = head

# printList(head)

print(detectLoop(head))
print(detectLoopSlowFast(head))
print(detectLoopMarkingVisited(head))
