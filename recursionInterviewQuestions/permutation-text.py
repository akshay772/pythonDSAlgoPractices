def permutationText(text):
    """
    Does not work. No way to generalize the solution

    :param text:
    :return:
    """
    combination = []
    for char in text:
        rest = text.replace(char, '')
        if len(rest) > 1:
            for char2 in rest:
                rest2 = text.replace(char2, rest)
                if len(rest2) > 1:
                    for char3 in rest2:
                        rest3 = text.replace(char3, rest)
                    combination.append(char + char2 + rest3)

    print(combination)


def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permuteRecursive(text, start, end, output=None):
    """
    Create a function permute() with parameters as input string, starting index of the string, ending index of the
    string Call this function with values input string, 0, size of string – 1 In this function, if the value of  L
    and R is the same then print the same string Else run a for loop from L to R and swap the current element in the
    for loop with the inputString[L] Then again call this same function by increasing the value of L by 1 After that
    again swap the previously swapped values to initiate backtracking

    :param end:
    :param start:
    :param text:
    :param output:
    :return:
    """
    if output is None:
        output = []

    if start == end:
        output.append(toString(text))

    else:
        for i in range(start, end):
            text[start], text[i] = text[i], text[start]
            permuteRecursive(text, start + 1, end, output)
            # For back-tracking that means to revert back to original position of the strin
            text[start], text[i] = text[i], text[start]

    return output


def permuteRecursiveAnother(text):
    out = []

    if len(text) == 1:
        out = [text]

    else:
        for i, letter in enumerate(text):
            for perm in permuteRecursiveAnother(text[:i] + text[i + 1:]):
                out += [letter + perm]

    return out


a = 'abc'
# permutationText(a)
print(permuteRecursive(list(a), 0, len(a)))
print(permuteRecursiveAnother(a))
