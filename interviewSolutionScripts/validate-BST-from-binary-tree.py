"""
    Validate if Binary Tree is a  Binary Search Tree

    A binary search tree (BST) is a node-based binary tree data structure that has the following properties.
    * The left subtree of a node contains only nodes with keys less than the node’s key.
    * The right subtree of a node contains only nodes with keys greater than the node’s key.
    * Both the left and right subtrees must also be binary search trees.
    * Each node (item in the tree) has a distinct key.
"""


# Python program to check if a binary tree is bst or not
# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:
    """
    Initialization of a Binary Tree Class
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxValue(node):
    """
    Returns maximum value in the node

    :param node:
    :return:
    """
    if node is None:
        return 0

    leftMax = maxValue(node.left)
    rightMax = maxValue(node.right)

    value = 0
    if leftMax > rightMax:
        value = leftMax
    else:
        value = rightMax

    if value < node.data:
        value = node.data

    return value


def minValue(node):
    """
    Returns minimum value in the node

    :param node:
    :return:
    """
    if node is None:
        return 1000000000

    leftMax = minValue(node.left)
    rightMax = minValue(node.right)

    value = 0
    if leftMax < rightMax:
        value = leftMax
    else:
        value = rightMax

    if value > node.data:
        value = node.data

    return value


# Returns true if a binary tree is a binary search tree
def isBST(node):
    """
    * If the current node is null then return true
    * If the value of the left child of the node is greater than or equal to the current node then return false
    * If the value of the right child of the node is less than or equal to the current node then return false
    * If the left subtree or the right subtree is not a BST then return false
    * Else return true\n

    Time Complexity: O(N2), As we visit every node just once and our helper method also takes O(N) time, so overall
    time complexity becomes O(N) * O(N) = O(N2)\n

    Auxiliary Space: O(H), Where H is the height of the binary tree,
    and the extra space is used due to the function call stack.\n

    :param node:
    :return:
    """
    if node is None:
        return True

    # false if the max of the left is > than us
    if node.left is not None and maxValue(node.left) > node.data:
        return False

    # false if the min of the right is <= than us
    if node.right is not None and minValue(node.right) < node.data:
        return False

    # false if, recursively, the left or right is not a BST
    if isBST(node.left) is False or isBST(node.right) is False:
        return False

    # passing all that, it's a BST
    return True


INT_MAX = 4294967296
INT_MIN = -4294967296


def isBSTEfficient(node):
    """
    This method is not applicable if there are duplicate elements with the value INT_MIN or INT_MAX.\n

    Follow the below steps to solve the problem:\n
    Call the isBstUtil function for the root node and set the minimum value as INT_MIN and the maximum value as INT_MAX
    If the current node is NULL then return true If the value of the node is less than the minimum value possible or
    greater than the maximum value possible then return false Call the same function for the left and the right subtree
    and narrow down the minimum and maximum values for these calls accordingly\n

    :param node:
    :return:
    """
    return isBSTUtil(node, INT_MIN, INT_MAX)


def isBSTUtil(node, minimum, maximum):
    """
    helper function to find if validation failed recursively

    :param node:
    :param minimum:
    :param maximum:
    :return:
    """
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < minimum or node.data > maximum:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return isBSTUtil(node.left, minimum, node.data - 1) and isBSTUtil(node.right, node.data + 1, maximum)


def treeMax(node):
    """
    Returns maximum value in the tree

    :param node:
    :return:
    """
    if node is None:
        return float('-inf')

    maxLeft = treeMax(node.left)
    maxRight = treeMax(node.right)

    return max(node.data, maxLeft, maxRight)


def treeMin(node):
    """
    Returns minimum value in the tree

    :param node:
    :return:
    """
    if node is None:
        return float('inf')

    minLeft = treeMin(node.left)
    minRight = treeMin(node.right)

    return max(node.data, minLeft, minRight)


def isBSTUdemySolution(node):
    """
    * If the current node is null then return true
    * If the value of the left child of the node is greater than or equal to the current node then return false
    * If the value of the right child of the node is less than or equal to the current node then return false
    * If the left subtree or the right subtree is not a BST then return false
    * Else return true\n

    Time Complexity: O(N2), As we visit every node just once and our helper method also takes O(N) time, so overall
    time complexity becomes O(N) * O(N) = O(N2)\n

    Auxiliary Space: O(H), Where H is the height of the binary tree,
    and the extra space is used due to the function call stack.\n

    :param node:
    :return:
    """
    if node is None:
        return True

    if treeMax(node.left) <= node.data <= treeMin(node.right) and isBSTUdemySolution(node.left) \
            and isBSTUdemySolution(node.right):
        return False

    else:
        return True


# TODO: Not working
def isBSTUsingInOrder(node, prev):
    """
    * Do In-Order Traversal of the given tree and store the result in a temp array.
    * This method assumes that there are no duplicate values in the tree
    * Check if the temp array is sorted in ascending order, if it is, then the tree is BST.\n

    Time Complexity: O(N), Where N is the number of nodes in the tree\n
    Auxiliary Space: O(H), Here H is the height
    of the tree and the extra space is used due to the function call stack.\n

    :param prev:
    :param node:
    :return:
    """
    # traverse the tree in inorder fashion
    # and keep track of prev node
    if node is not None:
        if isBSTUsingInOrder(node.left, prev):
            return False

        # Allows only distinct valued nodes
        if (prev is not None and
                node.data <= prev.data):
            return False

        prev = node
        return isBSTUsingInOrder(node.right, prev)

    return True


# Driver code
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)

    # Function call
    if isBST(root) is True:
        print("Is BST")
    else:
        print("Not a BST")

    # Function call
    if isBSTEfficient(root) is True:
        print("Is BST Efficient")
    else:
        print("Not a BST Efficient")

    # Function call
    if isBSTUdemySolution(root) is True:
        print("Is BST UdemySolution")
    else:
        print("Not a BST UdemySolution")

    # Function call
    previous = None
    if isBSTUsingInOrder(root, previous):
        print("Is BST UsingInOrder")
    else:
        print("Not a BST UsingInOrder")
