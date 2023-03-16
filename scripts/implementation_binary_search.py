"""
    Implementation of Binary Search
"""


def binarySearchRecursive(arr, ele):
    """
    Recursive implementation of binary search

    :param arr:
    :param ele:
    :return:
    """
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return binarySearchRecursive(arr[:mid], ele)
            else:
                return binarySearchRecursive(arr[mid+1:], ele)


def binarySearchIterative(arr, ele):
    """
    Iterative implementation of binary search

    :param arr:
    :param ele:
    :return:
    """
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    print(binarySearchIterative(a, 10))
    print(binarySearchRecursive(a, 1))
