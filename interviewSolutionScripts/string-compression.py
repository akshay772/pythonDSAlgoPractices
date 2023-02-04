def compressString(text):
    """
    Create a frequency map of characters and return key+value as string

    Time Complexity: O(N)\n
    Auxiliary Space: O(N)

    :param text:
    :return:
    """
    hashMap = {}
    compressed = ''

    for ele in text:
        if ele in hashMap:
            hashMap[ele] += 1
        else:
            hashMap[ele] = 1

    for key in hashMap:
        compressed += key + str(hashMap[key])

    return compressed


def compressStringRunLengthAlgo(text):
    """
    Implementation of Run Length ALgorithm which is compressing without checking

    Time Complexity: O(N)\n
    Auxiliary Space: O(N)

    :param text:
    :return:
    """
    length = len(text)
    compressed = ''

    if length == 0:
        return ''

    if length == 1:
        return text+'1'

    count = 1
    i = 1

    while i < length:
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed = compressed + text[i - 1] + str(count)
            count = 1
        i += 1

    compressed = compressed + text[i - 1] + str(count)

    return compressed


s = 'AAAABBBBCCCCCDDEEEE'
print(s)
print(compressStringRunLengthAlgo(s))