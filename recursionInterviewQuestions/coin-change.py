def coinChange(target, coins):
    minCoins = target

    if target in coins:
        return 1

    else:
        for i in [c for c in coins if c <= target]:
            numCoins = 1 + coinChange(target - i, coins)

            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins


# known_results is implementation of DP
def coinChangeUsingDP(target, coins, known_results):
    # Default output to target
    minCoins = target

    # Base case
    if target in coins:
        known_results[target] = 1
        return 1

    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]

    else:
        # For every coin value ie <= target
        for i in [c for c in coins if c <= target]:
            numCoins = 1 + coinChangeUsingDP(target - i, coins, known_results)

            if numCoins < minCoins:
                minCoins = numCoins

                # Reset that known result
                known_results[target] = minCoins

    return minCoins


# inefficient coz takes lots of time for below input
# since we are not tracking already solved sub-problems ( here it means sums )
# every combination is being solved and hence taking time
n = 122
cl = [1, 5, 10, 25]
solved_sub_problems = [0]*(n+1)
# print(coinChange(n, cl))
print(coinChangeUsingDP(n, cl, solved_sub_problems))
