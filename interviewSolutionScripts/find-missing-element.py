def findMissingElement(arr, shuffledArr):
    """
    consider every element of first array and increment the frequency. Similarly, decrement the frequency while
    traversing the shuffled array. search in second array. Return the positive frequency key.

    Time complexity of this solution is O(n)

    :param arr:
    :param shuffledArr:
    :return :
    """
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in shuffledArr:
        if num in freq:
            freq[num] -= 1

    for key, value in freq.items():
        if value > 0:
            return key


def missingNumber(arr, shuffledArr):
    """
    based on XOR. The combined occurrence of each element is twice, one in ‘arr1’ and other in ‘arr2’, except one
    element which only has a single occurrence in ‘arr1’. We know that (a Xor a) = 0. So, simply XOR the elements of
    both the arrays. The result will be the missing number.

    Time Complexity:  O(n).\n
    Space Complexity: O(1).

    :param arr:
    :param shuffledArr:
    :return missing:
    """
    # missing number 'missingNum'
    missingNum = 0

    # 1st array is of size 'n'
    for i in range(len(arr)):
        missingNum = missingNum ^ arr[i]

    # 2nd array is of size 'n - 1'
    for i in range(len(arr) - 1):
        missingNum = missingNum ^ shuffledArr[i]

    # Required missing number
    return missingNum


# Driver Code
arr1 = [4, 8, 1, 3, 7]
arr2 = [7, 4, 3, 1]
print("Missing number = ", missingNumber(arr1, arr2))

print(findMissingElement([1, 2, 3, 4, 5, 6, 6, 7], [3, 7, 2, 1, 4, 6]))
