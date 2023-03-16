"""Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the
new tree are between min and max (inclusive). The resulting tree should still be a valid binary search tree"""


class Node(object):
    """
    Initialize a Binary tree class
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def trimBST(node, minVal, maxVal):
    """
    Removes keys outside given range.

    While traversing the tree there are two possible cases for every node.\n
    1. Node’s key is outside the given range. This case has two subcases.
        * Node’s key is smaller than the min value.
        * Node’s key is greater than the max value.
    2. Node’s key is in range.
        * We don’t need to do anything for case 2. In case 1, we need to remove the node and change the root of the
        subtree rooted with this node.

    * In case 1 part 1, we simply remove the root and return the right subtree as a new root.
    * In case 1 part 2, we remove the root and return the left subtree as a new root.\n

    Time Complexity: O(N)\n
    Auxiliary Space: O(1)\n

    :param node:
    :param minVal:
    :param maxVal:
    :return:
    """
    if node is None:
        return None

    # First fix the left and right
    # subtrees of root
    node.left = trimBST(node.left, minVal, maxVal)
    node.right = trimBST(node.right, minVal, maxVal)

    # Now fix the root. There are 2
    # possible cases for root
    # 1.a Root's key is smaller than
    #      min value (root is not in range)
    if node.key < minVal:
        rightChild = node.right
        return rightChild

    # 1.b Root's key is greater than max
    #      value (root is not in range)
    if node.key > maxVal:
        leftChild = node.left
        return leftChild

    # 2. Root is in range
    return node


def trimBSTUdemy(node, minVal, maxVal):
    """
    Removes out of ranges keys from BST using Post-Order traversal. This way we trim left nodes, then right nodes and
    then root node. So once we reach root node, it is ensured that root's left and right node is a valid BST

    :param node:
    :param minVal:
    :param maxVal:
    :return:
    """
    if not node:
        return

    node.left = trimBSTUdemy(node.left, minVal, maxVal)
    node.right = trimBSTUdemy(node.right, minVal, maxVal)

    if minVal <= node.key <= maxVal:
        return node

    # if key is less than minimum value then node.left should be discarded due to BST property
    if node.key <= minVal:
        return node.right
    # if key is greater than maximum value then node.right should be discarded due to BST property
    if node.key >= maxVal:
        return node.left


def insert(node, key):
    """
    A utility function to insert a given key to BST
    :param node:
    :param key:
    :return:
    """
    if node is None:
        return Node(key)
    if node.key > key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def inorderTraversal(node):
    """
    Utility function to traverse the binary tree after conversion
    :param node:
    :return:
    """
    if node:
        inorderTraversal(node.left)
        print(node.key, end=" ")
        inorderTraversal(node.right)


if __name__ == '__main__':
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.right.left = Node(6)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    root = None
    root = insert(root, 6)
    root = insert(root, -13)
    root = insert(root, 14)
    root = insert(root, -8)
    root = insert(root, 15)
    root = insert(root, 13)
    root = insert(root, 7)
    inorderTraversal(root)

    root = trimBST(root, -10, 13)
    print()
    print("Inorder traversal of the modified tree is:")
    inorderTraversal(root)
    print()
    print()
    root = None
    root = insert(root, 6)
    root = insert(root, -13)
    root = insert(root, 14)
    root = insert(root, -8)
    root = insert(root, 15)
    root = insert(root, 13)
    root = insert(root, 7)
    inorderTraversal(root)
    root = trimBSTUdemy(root, -10, 13)
    print()
    print("Inorder traversal of the modified tree is:")
    inorderTraversal(root)
