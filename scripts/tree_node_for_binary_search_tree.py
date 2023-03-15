"""
    Implementation of Tree Node for BST
"""


class TreeNode(object):
    """
    Initialization of Tree Node Class for BST
    """
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        """
        Returns the Left Child of BST

        :return:
        """
        return self.leftChild

    def hasRightChild(self):
        """
        Returns the Right Child of BST

        :return:
        """
        return self.rightChild

    def isLeftChild(self):
        """
        If left child is a root
        :return:
        """
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """
        If right child is a root
        :return:
        """
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """
        Returns if root

        :return:
        """
        return not self.parent

    def isLeaf(self):
        """
        Returns if leaf

        :return:
        """
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        """
        Returns if left or right or both are present

        :return:
        """
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        """
        Returns if both children are present

        :return:
        """
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        """
        Modify data at Node in BST

        :param key:
        :param value:
        :param lc:
        :param rc:
        :return:
        """
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc

        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


