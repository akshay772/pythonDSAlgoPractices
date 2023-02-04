def compressString(text):
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