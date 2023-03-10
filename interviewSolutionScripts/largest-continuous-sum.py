def maxSumContinuousWrong(arr):
    """This won't work for obvious reasons as the next value may decrease the maximum but the whole sequence may end
    up increasing the maximum"""
    globalSum = 0
    currSum = 0

    for i in range(len(arr)):
        if currSum + arr[i] > currSum:
            currSum += arr[i]
        else:
            if currSum > globalSum:
                globalSum = currSum
            currSum = 0

    return globalSum


def maxSumContinuousKadaneAlgorithm(arr):
    """
    Kadane’s algorithm is to maintain a variable max_ending_here that stores the maximum sum contiguous subarray
    ending at current index and a variable max_so_far stores the maximum sum of contiguous subarray found so far,
    Everytime there is a positive-sum value in max_ending_here compare it with max_so_far and update max_so_far if it
    is greater than max_so_far

    Time Complexity:  O(n).\n
    Space Complexity: O(1).

    :param arr:
    :return max_sum:
    """
    maxEndingHere = 0
    maxSoFar = 0
    start = 0
    end = 0
    init = 0

    for i in range(len(arr)):
        maxEndingHere = maxEndingHere + arr[i]

        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
            start = init
            end = i

        if maxEndingHere < 0:
            maxEndingHere = 0
            init = i + 1

    return maxSoFar


print(maxSumContinuousWrong([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(maxSumContinuousKadaneAlgorithm([1, 2, -1, 3, 4, 10, 10, -20, -10, -1, 20, 10, 10]))
