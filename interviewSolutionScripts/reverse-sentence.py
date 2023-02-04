def reverseSentence(sentence):
    """
    Store the string in the form of words. Run a for loop in reverse order to print the words accordingly

    Time Complexity: O(N)\n
    Auxiliary Space: O(N)

    :param sentence:
    :return:
    """
    reverse = ''
    sentence = sentence.split(' ')
    for i in range(len(sentence), 0, -1):
        if sentence[i - 1] == "":
            continue
        reverse += sentence[i - 1] + " "
    reverse = reverse[0:len(reverse) - 1]

    return reverse


def reverseSentenceUsingInsert(sentence):
    """
    Store the string in the form of words. Run a for loop and insert in reverse order to print the words accordingly

    Time Complexity: O(N)\n
    Auxiliary Space: O(N)

    :param sentence:
    :return:
    """
    words = sentence.split(' ')
    string = []
    for word in words:
        if word == "":
            continue
        string.insert(0, word)

    string = " ".join(string)
    return string


def reverseSentenceOneLiner(sentence):
    """
    Store the string in the form of words. Run a for loop in reverse order to print the words accordingly

    Time complexity: O(N2)\n
    Auxiliary Space: O(N)

    :param sentence:
    :return:
    """
    sentence = sentence.split()[::-1]

    # joining the reversed string and
    # printing the output
    sentence = " ".join(sentence)

    return sentence


def reverseSentenceUsingSwap(sentence):
    """
    Store the string in the form of words
    Swap the words with each other starting from the middle
    Print the string

    Time complexity: O(N)\n
    Auxiliary Space: O(N)

    :param sentence:
    :return:
    """
    sentence = sentence.split(' ')
    sentence = list(filter(None, sentence))
    length = len(sentence)
    midP = 0
    if length % 2 == 0:
        midP = int(length/2)
    else:
        midP = int(length/2 + 1)

    while midP <= length - 1:
        sentence[midP], sentence[length - midP - 1] = sentence[length - midP - 1], sentence[midP]
        midP += 1

    sentence = ' '.join(sentence)
    return sentence


def reverseWord(sentence, start, end):
    while start < end:
        sentence[start], sentence[end] = sentence[end], sentence[start]
        start += 1
        end -= 1


def reverseSentenceUsingIndividualReverse(sentence):
    """
    Initially, reverse the individual words of the given string one by one, for the above example, after reversing
    individual words the string should be “i ekil siht margorp yrev hcum”. Reverse the whole string from start to end
    to get the desired output “much very program this like i” in the above example.

    :param sentence:
    :return:
    """
    sentence = list(sentence)
    start = 0

    while True:
        # We use a try catch block because for the last word the list.index() function returns a ValueError as it cannot
        # find a space in the list
        try:
            # Find the next space
            end = sentence.index(' ', start)

            # Reverse each word one by one in loop
            reverseWord(sentence, start, end - 1)

            # Update start variable
            start = end + 1

        except ValueError:
            # Reverse the last word
            reverseWord(sentence, start, len(sentence) - 1)
            break

    sentence.reverse()

    sentence = ''.join(sentence)
    sentence = sentence.strip()

    return sentence


text = 'Hi John,   are you ready to go?'
text = '    space before'

print(text)
print(len(text))
print(reverseSentenceUsingIndividualReverse(text))
print(len(reverseSentenceUsingIndividualReverse(text)))
print(reverseSentenceUsingSwap(text))
print(len(reverseSentenceUsingSwap(text)))
