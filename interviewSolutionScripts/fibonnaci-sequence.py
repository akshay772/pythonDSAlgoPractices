def fibonacciSequence(num):
    if num == 1 or num == 2:
        return 1

    else:
        return fibonacciSequence(num - 1) + fibonacciSequence(num - 2)


def fibonacciSequence2(num):
    if num == 0 or num == 1:
        return num

    else:
        return fibonacciSequence(num - 1) + fibonacciSequence(num - 2)


def fibonacciIterative(num):
    a, b = 0, 1

    for i in range(num):
        a, b = b, a + b

    return a


# Cache
n = 10
cache = [None] * (n + 1)


def fibonacciSequenceCache(num):
    if num == 0 or num == 1:
        return num

    if cache[num] is not None:
        return cache[num]

    cache[num] = fibonacciSequenceCache(num - 1) + fibonacciSequenceCache(num - 2)

    return cache[num]


n = 10
print(fibonacciSequenceCache(n))
print(fibonacciSequence2(n))
print(fibonacciIterative(n))
print(fibonacciSequence(n))
