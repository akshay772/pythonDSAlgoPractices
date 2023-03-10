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
    Space Complexity: O(n).

    :param text:
    :return:
    """
    stack = []
    openBrackets = ['{', '[', '(']
    closeBrackets = ['}', ']', ')']
    for char in text:
        if char in openBrackets:
            stack.append(char)
        elif char in closeBrackets:
            pos = closeBrackets.index(char)
            if len(stack) > 0 and openBrackets[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


def balanceParenthesisCheckUsingStackAnother(text):
    """
    Using queue First Map opening parentheses to respective closing parentheses. Iterate through the given expression
    using ‘char’, if ‘char’ is an open parentheses, append in queue, if ‘char’ is close parentheses, Check whether
    queue is empty or ‘char’ is the top element of queue, if yes, return “Unbalanced”, otherwise “Balanced”.

    Time Complexity:  O(n).\n
    Space Complexity: O(n).

    :param text:
    :return:
    """
    openBrackets = tuple('{[(')
    closeBrackets = tuple('}])')
    firstMap = dict(zip(openBrackets, closeBrackets))
    stack = []

    for char in text:
        if char in openBrackets:
            stack.append(firstMap[char])
        elif char in closeBrackets:
            if not stack or char != stack.pop():
                return False

    if not stack:
        return True
    else:
        return False


def balanceParenthesisCheckUsingElimination(text):
    """
    Elimination based In every iteration, the innermost brackets get eliminated (replaced with empty string). If we
    end up with an empty string, our initial one was balanced; otherwise, not.

    Time Complexity:  O(n).\n
    Space Complexity: O(n).

    :param text:
    :return:
    """
    brackets = ['()', '[]', '{}']

    while any(char in text for char in brackets):
        for br in brackets:
            text = text.replace(br, '')

    return not text


def balanceParenthesisCheckUsingStackMatchingSet(text):
    """
    First we will scan the string from left to right, and every time we see an opening parenthesis we push it to a
    stack, because we want the last opening parenthesis to be closed first. (Remember the FILO structure of a stack!)
    Then, when we see a closing parenthesis we check whether the last opened one is the corresponding closing match,
    by popping an element from the stack. If it’s a valid match, then we proceed forward, if not return false. Or if
    the stack is empty we also return false, because there’s no opening parenthesis associated with this closing one.
    In the end, we also check whether the stack is empty. If so, we return true, otherwise return false because there
    were some opened parenthesis that were not closed.

    Time Complexity:  O(n).\n
    Space Complexity: O(n).

    :param text:
    :return:
    """
    openBracket = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []

    for bracket in text:
        if bracket in openBracket:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False

            lastOpenBracket = stack.pop()
            if (lastOpenBracket, bracket) not in matches:
                return False

    return len(stack) == 0


print(balanceParenthesisCheckUsingStacks('[](){([[[]]])}'))
print(balanceParenthesisCheckUsingStacks('[](){([[[]]])}(}}}{{{'))
print(balanceParenthesisCheckUsingStacks('{}}{'))

print(balanceParenthesisCheckUsingStackAnother('[](){([[[]]])}'))
print(balanceParenthesisCheckUsingStackAnother('[](){([[[]]])}(}}}{{{'))
print(balanceParenthesisCheckUsingStackAnother('{}}{'))

print(balanceParenthesisCheckUsingElimination('[](){([[[]]])}'))
print(balanceParenthesisCheckUsingElimination('[](){([[[]]])}(}}}{{{'))
print(balanceParenthesisCheckUsingElimination('{}}{'))

print(balanceParenthesisCheckUsingStackMatchingSet('[](){([[[]]])}'))
print(balanceParenthesisCheckUsingStackMatchingSet('[](){([[[]]])}(}}}{{{'))
print(balanceParenthesisCheckUsingStackMatchingSet('{}}{'))