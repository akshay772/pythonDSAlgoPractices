"""
    Implements method of traversing a Binary Tree
"""
from implementation_tree_using_OOP import BinaryTree


def traversePreOrder(tree: BinaryTree, count):
    """
    Function to traverse a Binary Tree Pre-order
    :param count:
    :param tree:
    :return:
    """
    if tree:
        count += 1
        print(count, tree.getRootVal())
        traversePreOrder(tree.getLeftChild(), count)
        traversePreOrder(tree.getRightChild(), count)


def traversePostOrder(tree: BinaryTree):
    """
    Function to traverse a Binary Tree Post-order
    :param tree:
    :return:
    """
    if tree:
        traversePostOrder(tree.getLeftChild())
        traversePostOrder(tree.getRightChild())
        print(tree.getRootVal())


def traverseInOrder(tree: BinaryTree):
    """
    Function to traverse a Binary Tree In-order
    :param tree:
    :return:
    """
    if tree:
        traversePreOrder(tree.getLeftChild())
        print(tree.getRootVal())
        traversePreOrder(tree.getRightChild())


# Driver code
if __name__ == "__main__":
    bt = BinaryTree('1')
    bt.insertLeft('2')
    bt.insertRight('3')
    bt.leftChild.insertLeft('4')
    bt.leftChild.insertRight('5')
    bt.rightChild.insertLeft('6')
    bt.rightChild.insertRight('7')

    print('Pre-Oder traversal')
    traversePreOrder(bt, 0)
    # bt.traversePreOrder()
    print('Post-Oder traversal')
    traversePostOrder(bt)
    # bt.traversePostOrder()
    print('In-Oder traversal')
    bt.traverseInOrder()
