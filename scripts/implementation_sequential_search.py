"""
    Implementation of sequential search for ordered and un-ordered list
"""


def seqSearchUnOrdered(arr, ele):
    """
    Sequentially search for the ele in unordered list

    :param arr:
    :param ele:
    :return:
    """
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True

        else:
            pos += 1

    return found


def seqSearchOrdered(arr, ele):
    """
    Sequentially search for the ele in ordered/sorted list

    :param arr:
    :param ele:
    :return:
    """
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1

    return found


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(seqSearchUnOrdered(arr, 5))
    print(seqSearchUnOrdered(arr, 12))
