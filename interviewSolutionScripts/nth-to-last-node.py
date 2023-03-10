class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


def printList(headNode):
    temp = headNode

    while temp:
        print(temp.value, end=" ==> ")
        temp = temp.nextNode


def reverse(headNode):
    prevNode = None
    currNode = headNode
    while currNode is not None:
        nextNode = currNode.nextNode
        currNode.nextNode = prevNode
        prevNode = currNode
        currNode = nextNode

    return prevNode


def nthToLastNodeReverse(val, headNode):
    """
    Reverse a linked list and increment counter till val is reached\n

    Time Complexity: O(N), Traversing over the linked list of size N\n
    Auxiliary Space: O(1)\n

    :param val:
    :param headNode:
    :return:
    """
    targetNode = headNode
    length = 0
    while targetNode is not None:
        targetNode = targetNode.nextNode
        length += 1

    if val > length:
        print('location should not be greater than length of the list')

    targetNode = headNode
    targetNode = reverse(targetNode)
    count = 1
    while count < val:
        targetNode = targetNode.nextNode
        count += 1

    return targetNode.value


def nthToLastNodeLength(val, headNode):
    """
    Calculate the length of the Linked List. Let the length be len.
    Print the (len – n + 1)th node from the beginning of the Linked List.\n

    Time complexity: O(M) where M is the size of the linked list\n
    Auxiliary Space: O(1)\n

    :param val:
    :param headNode:
    :return:
    """
    targetNode = headNode

    length = 0
    while targetNode is not None:
        targetNode = targetNode.nextNode
        length += 1

    if val > length:
        print('location should not be greater than length of the list')
        return

    targetNode = headNode
    for i in range(0, length - val):
        targetNode = targetNode.nextNode

    return targetNode.value


def nthToLastNodeLengthRecursive(val, headNode):
    i = 0
    if headNode is None:
        return

    nthToLastNodeLengthRecursive(val, headNode.nextNode)
    i += 1
    if i == val:
        print(headNode.value)
        return headNode.value


def nthToLastNodeTwoPointerLength(val, headNode):
    """
    As Nth node from the end equals to (Length – N + 1)th node from the start, so the idea is to Maintain two
    pointers starting from the head of the Linked-List and move one pointer to the Nth node from the start and then
    move both the pointers together until the pointer at the Nth position reaches the last node. Now the pointer
    which was moved later points at the Nth node from the end of the Linked-List\n

    Time Complexity: O(M) where M is the length of the linked list.\n
    Auxiliary Space: O(1)\n

    :param val: number
    :param headNode: head of linked-list
    :return:
    """
    referNode = headNode
    mainNode = headNode

    count = 0
    if headNode is not None:
        while count < val:
            if referNode is None:
                raise LookupError('%d location should not be greater than length of the list' % val)

            referNode = referNode.nextNode
            count += 1

    if referNode is None:
        headNode = headNode.nextNode
        if headNode is not None:
            print('Node no. %d from last is %d ' % (val, mainNode.value))
            return mainNode.value

    else:
        while referNode is not None:
            mainNode = mainNode.nextNode
            referNode = referNode.nextNode

        print('Node no. %d from last is %d ' % (val, mainNode.value))
        return mainNode.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e

# print(nthToLastNodeReverse(3, a))
# print(nthToLastNodeLength(3, a))
# print(nthToLastNodeLengthRecursive(3, a))
print(nthToLastNodeTwoPointerLength(4, a))
