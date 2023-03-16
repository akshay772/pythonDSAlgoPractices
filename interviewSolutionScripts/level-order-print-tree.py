"""
    Prints the keys of Binary Search Tree in Level Order
"""
import collections
import os


class Node(object):
    """
    Initialize a Binary Tree Class
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def traversePreOrder(node, count, arr):
    """
    Pre Order traversal of Tree

    :param arr:
    :param count:
    :param node:
    :return:
    """
    if node is not None:
        count += 1
        if count not in arr:
            arr[count] = str(node.key)
        else:
            arr[count] += ' ' + str(node.key)
        traversePreOrder(node.left, count, arr)
        traversePreOrder(node.right, count, arr)


def printLevelOrder(node):
    """
    Prints key in level order fashion
    :param node:
    :return:
    """
    count = -1
    arr = {}
    traversePreOrder(node, count, arr)
    printLevel = ''''''
    for key, value in arr.items():
        printLevel += value + os.linesep

    print(printLevel)
    return printLevel


def printLevelOrderDeptFirstSearch(node):
    """
    A simple solution is to print using the recursive function discussed in the level order traversal post and print
    a new line after every call to printGivenLevel().Find height of tree and run depth first search and maintain
    current height, print nodes for every height from root and for 1 to height.\n

    Time complexity: O(N2)\n
    Auxiliary Space: O(N)\n

    :param node:
    :return:
    """
    h = height(node)

    for i in range(0, h + 1):
        printGivenLevel(node, i)
        print()


def printGivenLevel(node, level):
    """
    Helper function to traverse and return the node

    :param node:
    :param level:
    :return:
    """
    if node is None:
        return node

    if level == 1:
        print(node.key, end=' ')
    elif level > 1:
        printGivenLevel(node.left, level - 1)
        printGivenLevel(node.right, level - 1)


def height(node):
    """
    Compute the height of a tree--the number of nodes along the longest path from the root node down to the farthest
    leaf node

    :param node:
    :return:
    """
    if node is None:
        return 0
    else:
        leftHeight = height(node.left)
        rightHeight = height(node.right)

        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1


def printLevelOrderIterativeQueue(node):
    """
    The idea is to keep a queue that stores nodes of the current level. Starting from root, calculate the size of
    queue sz and for each one of sz nodes enqueue its children to queue and print the node. After printing sz nodes
    of every iteration print a line break.\n

    Time complexity: O(N) where n is no of nodes of binary tree\n
    Auxiliary Space: O(N) for queue\n

    :param node:
    :return:
    """
    if node is None:
        return

    queue = [node]
    while queue:
        # nodeCount (queue size) indicates number
        # of nodes at current level.
        count = len(queue)

        # Dequeue all nodes of current level and
        # Enqueue all nodes of next level
        while count > 0:
            temp = queue.pop(0)
            print(temp.key, end=' ')
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

            count -= 1
        print(' ')


def printLevelOrderDeque(node):
    """
    It won’t be practical to solve this problem using recursion, because recursion is similar to depth first search,
    but what we need here is breadth first search. So we will use a queue as we did previously in breadth first
    search. First, we’ll push the root node into the queue. Then we start a while loop with the condition queue not
    being empty. Then, at each iteration we pop a node from the beginning of the queue and push its children to the
    end of the queue. Once we pop a node we print its value and space.\n To print the new line in correct place we
    should count the number of nodes at each level. We will have 2 counts, namely current level count and next level
    count. Current level count indicates how many nodes should be printed at this level before printing a new line.
    We decrement it every time we pop an element from the queue and print it. Once the current level count reaches
    zero we print a new line. Next level count contains the number of nodes in the next level, which will become the
    current level count after printing a new line. We count the number of nodes in the next level by counting the
    number of children of the nodes in the current level.

    :param node:
    :return:
    """
    if not node:
        return

    nodeDeque = collections.deque([node])
    currentCount = 1
    nextCount = 0

    while len(nodeDeque) != 0:
        currentNode = nodeDeque.popleft()
        currentCount -= 1
        print(currentNode.key, end=' ')

        if currentNode.left:
            nodeDeque.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodeDeque.append(currentNode.right)
            nextCount += 1
        if currentCount == 0:
            print()
            currentCount, nextCount = nextCount, currentCount


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(5)

    printLevelOrder(root)

    printLevelOrderDeptFirstSearch(root)

    printLevelOrderIterativeQueue(root)

    printLevelOrderDeque(root)
