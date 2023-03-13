"""
    Implements method of traversing a Binary Tree
"""
from implementation_tree_using_OOP import BinaryTree


def traversePreOrder(tree: BinaryTree):
    """
    Function to traverse a Binary Tree Pre-order
    :param tree:
    :return:
    """
    if tree:
        print(tree.getRootVal())
        traversePreOrder(tree.getLeftChild())
        traversePreOrder(tree.getRightChild())


def traversePostOrder(tree: BinaryTree):
    """
    Function to traverse a Binary Tree Post-order
    :param tree:
    :return:
    """
    if tree:
        traversePreOrder(tree.getLeftChild())
        traversePreOrder(tree.getRightChild())
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


bt = BinaryTree('a')
bt.insertLeft('b')
bt.insertRight('c')

print('Pre-Oder traversal')
traversePreOrder(bt)
# bt.traversePreOrder()
print('Post-Oder traversal')
traversePostOrder(bt)
# bt.traversePostOrder()
print('In-Oder traversal')
bt.traverseInOrder()
