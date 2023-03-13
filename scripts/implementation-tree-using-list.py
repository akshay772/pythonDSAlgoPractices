"""
    Implementation of a Binary Tree using List data-type
"""


def binaryTree(root):
    """
    Initialize a root node

    :param root:
    :return:
    """
    return [root, [], []]


def insertLeft(root, newBranch):
    """
    Insert left child at root node

    :param root:
    :param newBranch:
    :return:
    """
    temp = root.pop(1)

    if len(temp) > 1:
        root.insert(1, [newBranch, temp, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    """
    Insert right child at root node

    :param root:
    :param newBranch:
    :return:
    """
    temp = root.pop(2)

    if len(temp) > 1:
        root.insert(2, [newBranch, [], temp])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def getRootVal(root):
    """
    Get value at root node

    :param root:
    :return:
    """
    return root[0]


def setRootVal(root, newVal):
    """
    Set value of root node

    :param root:
    :param newVal:
    :return:
    """
    root[0] = newVal


def getLeftChild(root):
    """
    Get value at left child of root node

    :param root:
    :return:
    """
    return root[1]


def getRightChild(root):
    """
    Get value at right child of root node

    :param root:
    :return:
    """
    return root[2]


r = binaryTree(3)
print(insertLeft(r, 4))
print(insertLeft(r, 5))
print(insertRight(r, 6))
print(insertRight(r, 7))

left = getLeftChild(r)
print(left)
# Setting left value will affect original root since it still references root
setRootVal(left, 9)
print(left)
print(r)
