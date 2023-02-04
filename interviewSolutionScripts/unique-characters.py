def isUniqueChars(text):
    """
    Create a frequency map of characters and return True if frequency is 1 for every char else return False

    Time Complexity: O(N)\n
    Auxiliary Space: O(N)

    :param text:
    :return:
    """
    hashMap = {}

    for ele in text:
        if ele in hashMap:
            return False
        else:
            hashMap[ele] = 1

    return True


def isUniqueCharsOneLiner(text):
    """
    Using Set data-structure. Since length of Set is unique chars.

    Time Complexity: O(1)\n
    Auxiliary Space: O(1)

    :param text:
    :return:
    """
    return len(set(text)) == len(text)


def isUniqueCharsUsingSet(text):
    """
    Using Set data-structure. As it stores unique characters.

    Time Complexity: O(N)\n
    Auxiliary Space: O(N)

    :param text:
    :return:
    """
    chars = set()

    for ele in text:
        if ele in chars:
            return False
        else:
            chars.add(ele)

    return True




