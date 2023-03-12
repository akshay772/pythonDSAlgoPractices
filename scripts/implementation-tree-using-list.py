def BinaryTree(root):
    return [root, [], []]


def insertLeft(root, newBranch):
    temp = root.pop(1)

    if len(temp) > 1:
        root.insert(1, [newBranch, temp, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    temp = root.pop(2)

    if len(temp) > 1:
        root.insert(2, [newBranch, [], temp])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


r = BinaryTree(3)
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
