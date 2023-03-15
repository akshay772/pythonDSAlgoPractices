def reverseTextRecursive(text, i=0):
    text = list(text)
    n = len(text)

    if i == n // 2:
        return

    text[i], text[n - i - 1] = text[n - i - 1], text[i]

    reverseTextRecursive(text, i+1)

    return ''.join(text)


def reverseTextRecursiveSimple(text):
    if len(text) <= 1:
        return text

    return reverseTextRecursive(text[1:]) + text[0]


print(reverseTextRecursive('hello world'))
print(reverseTextRecursiveSimple('hello world'))
