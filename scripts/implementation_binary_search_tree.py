"""
    Implementation of Binary Search Tree
"""
from tree_node_for_binary_search_tree import TreeNode


class BinarySearchTree(object):
    """
    Initialization of Binary Search Tree Class
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        """
        Returns the length of binary search tree

        :return:
        """
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self: TreeNode):
        # Inorder iterative method
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
        yield self.key
        if self.hasRightChild():
            for elem in self.rightChild:
                yield elem

    def put(self, key, val):
        """
        Insert a key, val in BST

        :param key:
        :param val:
        :return:
        """
        if self.root:
            self._put(key, val, self.root)

        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)

        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        """
        Get key Node from BST

        :param key:
        :return:
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None

        elif currentNode.key == key:
            return currentNode

        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)

        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def delete(self, key):
        """
        Delete a key Node from tree

        :param key:
        :return:
        """
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1

        else:
            raise KeyError('Error, key not in tree')

    def __delete__(self, instance):
        self.delete(instance)

    def remove(self, currentNode):
        """
        Remove the current node from BST
        :param currentNode:
        :return:
        """
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren():  # interior
            successor = currentNode.findSuccessor()
            successor.spliceOut()
            currentNode.key = successor.key
            currentNode.payload = successor.payload

        else:  # has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild
                    )

            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild
                    )

    def findSuccessor(self: TreeNode):
        """
        Find the smallest value to be replaced down the node

        :return:
        """
        successor = None

        if self.hasRightChild():
            successor = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    successor = self.parent
                else:
                    self.parent.rightChild = None
                    successor = self.parent.findSuccessor()
                    self.parent.rightChild = self

        return successor

    def findMin(self):
        """
        Find minimum down the traversal

        :return:
        """
        current = self

        while current.hasLeftChild():
            current = current.leftChild()

        return current

    def spliceOut(self: TreeNode):
        """
        Disconnect self and re-organize rest of the nodes in BST

        :return:
        """
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None

        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent

        else:
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
