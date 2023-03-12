def sumDigitsInNum(num):
    if num == 0:
        return 0

    return num % 10 + int(sumDigitsInNum(num/10))


a = 4321
print(sumDigitsInNum(a))
