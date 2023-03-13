"""
    Implementation of a Binary Tree using Class/OOPs method
"""


class BinaryTree(object):
    """
    Initialize a Binary Tree Class
    """

    def __init__(self, rootObj):
        """
        Initialize root of a Binary Tree

        :param rootObj:
        """
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """
        Insert left child at root

        :param newNode:
        :return:
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, newNode):
        """
        Insert right child at root

        :param newNode:
        :return:
        """
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp

    def getRightChild(self):
        """
        Get the value of right child at root
        :return:
        """
        return self.rightChild

    def getLeftChild(self):
        """
        Get the value of left child at root

        :return:
        """
        return self.leftChild

    def setRootVal(self, obj):
        """
        Set the value of root

        :param obj:
        :return:
        """
        self.key = obj

    def getRootVal(self):
        """
        Get the value at root

        :return:
        """
        return self.key

    def traversePreOrder(self):
        """
        Traverse a Binary Tree in Pre-Order

        :param:
        :return:
        """
        if self.key:
            print(self.key)
            if self.leftChild:
                self.leftChild.traversePreOrder()
            if self.rightChild:
                self.rightChild.traversePreOrder()

    def traversePostOrder(self):
        """
        Traverse a Binary Tree in Post-Order

        :param:
        :return:
        """
        if self.leftChild:
            self.leftChild.traversePreOrder()
        if self.rightChild:
            self.rightChild.traversePreOrder()
        print(self.key)

    def traverseInOrder(self):
        """
        Traverse a Binary Tree in In-Order

        :param:
        :return:
        """
        if self.leftChild:
            self.leftChild.traversePreOrder()
        print(self.key)
        if self.rightChild:
            self.rightChild.traversePreOrder()

# r = BinaryTree('a')
# print(r.getRootVal())

# r.insertLeft('b')
# print(r.getLeftChild().getRootVal())
