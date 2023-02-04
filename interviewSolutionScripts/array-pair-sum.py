def countPairSum(arr, val):
    """
    Using Brute Force method by running n^2 loop to check if sum equals given value

    Time Complexity: O(N^2), For looping.\n
    Auxiliary Space: O(1) as it is using constant extra space

    :param val:
    :param arr:
    :param sum:
    :return count:
    """
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == val:
                count += 1

    return count


def getUnOrderedPairSumUsingSetSeenTrack(arr, val):
    """
    Time Complexity: O(N), For looping.\n
    Auxiliary Space: O(1) as it is using constant extra space

    :param arr:
    :param val:
    :return count:
    """
    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    for i, num in enumerate(arr):
        target = val - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return len(output)


def countOrderedPairSumUsingHasMap(arr, val):
    """
    The idea is to create a map of frequency of each number present in the array. in the next traversal,
    for every element check if it can be combined with any other element to give the desired sum. If so,
    increment the counter but check if the [arr[i], arr[i]] pair forms then reduce count by 1 to discard such
    combination. After the completion of 2nd traversal, we'd have twice the required value stored in the counter.
    Hence divide the count by 2 and return.

    Time Complexity: O(N), For looping.\n
    Auxiliary Space: O(N) as it is using constant extra space

    :param arr:
    :param val:
    :return count:
    """
    hashMap = {}
    pairs = []
    twiceCount = 0

    for num in arr:
        if num in hashMap:
            hashMap[num] += 1
        else:
            hashMap[num] = 1

    for i in range(len(arr)):
        if val - arr[i] in hashMap:
            # here val - arr[i] is acting as a complement to arr[i] wrt val
            twiceCount += hashMap[val - arr[i]]

            if (val - arr[i]) == arr[i]:
                # meaning [arr[i], arr[i]] pair found
                twiceCount -= 1

    return int(twiceCount / 2)


print(countOrderedPairSumUsingHasMap([1, 2, 3, 1, 1], 3))

print(countOrderedPairSumUsingHasMap([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 6))

print(getUnOrderedPairSumUsingSetSeenTrack([1, 2, 3, 1, 1], 3))
