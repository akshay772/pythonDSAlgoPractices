def factorial(val):
    # Base Case
    if val == 0:
        return 1

    else:
        return val * factorial(val - 1)


# Create cache for known results
factorial_memo = {}


def factorialWithMemoization(val):
    if val < 2:
        return 1

    if val not in factorial_memo:
        factorial_memo[val] = val * factorial(val - 1)

    return factorial_memo[val]


class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


factorial = Memoize(factorial)

print(factorial(5))
print(factorialWithMemoization(5))
