def balanceParenthesisCheck(text):
    """
    Applying brute-force thinking by iterating over characters and keeping counts of closing and opening counts. Will
    not work in case of nested unordered closing-opening brackets.

    Time Complexity:  O(n).\n
    Space Complexity: O(1).

    :param text:
    :return {bool}:
    """
    squareCount = 0
    curlyCount = 0
    roundCount = 0

    for char in text:
        if char == '[':
            squareCount += 1
        elif char == ']':
            squareCount -= 1
        elif char == '{':
            curlyCount += 1
        elif char == '}':
            curlyCount -= 1
        elif char == '(':
            roundCount += 1
        elif char == ')':
            roundCount -= 1

    if squareCount == curlyCount == roundCount == 0:
        return True
    else:
        return False


def balanceParenthesisCheckUsingStacks(text):
    """
    Using stack One approach to check balanced parentheses is to use stack. Each time, when an open parentheses is
    encountered push it in the stack, and when closed parenthesis is encountered, match it with the top of stack and
    pop it. If stack is empty at the end, return Balanced otherwise, Unbalanced.

    Time Complexity:  O(n).\n
    Space Complexity: O(1).

    :param text:
    :return:
    """


print(balanceParenthesisCheck('[](){([[[]]])}('))
print(balanceParenthesisCheck('[](){([[[]]])}(}}}{{{'))
print(balanceParenthesisCheck('{}}{'))
