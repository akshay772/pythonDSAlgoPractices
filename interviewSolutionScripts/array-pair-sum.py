def countPairSum(arr, val):
    """
    Using Brute Force method by running n^2 loop to check if sum equals given value

    Time Complexity: O(N^2), For looping.
    Auxiliary Space: O(1) as it is using constant extra space

    :param arr:
    :param sum:
    :return number:
    """
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == val:
                count += 1

    return count


def getPairSum(arr, val):

    pass


def countPairSumUsingHasMap(arr, val):
    """
    The idea is to create a map of frequency of each number present in the array. in the next traversal,
    for every element check if it can be combined with any other element to give the desired sum. If so,
    increment the counter but check if the [arr[i], arr[i]] pair forms then reduce count by 1 to discard such
    combination. After the completion of 2nd traversal, we'd have twice the required value stored in the counter.
    Hence divide the count by 2 and return

    Time Complexity: O(N), For looping.
    Auxiliary Space: O(N) as it is using constant extra space

    :param arr:
    :param val:
    :return number:
    """
    hashMap = {}
    twiceCount = 0

    for num in arr:
        if num in hashMap:
            hashMap[num] += 1
        else:
            hashMap[num] = 1

    for i in range(len(arr)):
        if val - arr[i] in hashMap:
            twiceCount += hashMap[val - arr[i]]

            if (val - arr[i]) == arr[i]:
                # meaning [arr[i], arr[i]] pair found
                twiceCount -= 1

    return int(twiceCount / 2)


print(pairSumUsingHasMap([1, 2, 3, 1], 3))
