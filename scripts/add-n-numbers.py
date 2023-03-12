def sumOfNNumbers(val):
    if val == 0:
        return 0

    return val + sumOfNNumbers(val - 1)


num = 100
print(sumOfNNumbers(num))
