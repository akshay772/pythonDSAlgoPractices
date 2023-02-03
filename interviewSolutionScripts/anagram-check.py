import re


def removeNonAlphaNumeric(text):
    """
    Remove spaces, punctuations and returns lowercase text
    :param text:
    :return text:
    """
    text = text.replace(" ", "")
    text = text.replace(".", "")
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', text)

    return text.lower()


def equalLength(text, anotherText):
    """
    Compares the length of text with anotherText and return a boolean value
    :param text:
    :param anotherText:
    :return boolean:
    """
    if len(text) == len(anotherText):
        return True
    else:
        return False


def anagram(text, anotherText):
    """
    Sort the two given strings and compare, if they are equal then they are anagram of each other.

    Time Complexity: O(N * logN), For sorting.
    Auxiliary Space: O(1) as it is using constant extra space

    :param text:
    :param anotherText:
    :return boolean:
    """
    text = removeNonAlphaNumeric(text)
    anotherText = removeNonAlphaNumeric(anotherText)

    if sorted(text) == sorted(anotherText):
        return True
    else:
        return False


def anagramUsingCharCount(text, anotherText):
    """
    The idea is based in an assumption that the set of possible characters in both strings is small. that the
    characters are stored using 8 bit and there can be 256 possible characters.

    So count the frequency of the characters and if the frequency of characters in both strings are the same,
    they are anagram of each other.

    Time Complexity: O(n)
    Auxiliary Space: O(256) i.e. O(1) for constant space.

    :param text:
    :param anotherText:
    :return boolean:
    """
    text = removeNonAlphaNumeric(text)
    anotherText = removeNonAlphaNumeric(anotherText)

    if not equalLength(text, anotherText):
        return False

    numOfChars = 256

    charsCountText = [0] * numOfChars
    charsCountAnotherText = [0] * numOfChars

    for i in text:
        charsCountText[ord(i)] += 1
    for i in anotherText:
        charsCountAnotherText[ord(i)] += 1

    for i in range(numOfChars):
        if charsCountText[i] != charsCountAnotherText[i]:
            return False

    return True


def anagramUsingOneCount(text, anotherText):
    """
    The above can be modified to use only one count array instead of two. Increment the value in count array for
    characters in str1 and decrement for characters in str2. Finally, if all count values are 0, then the two strings
    are anagram of each other.

    Time Complexity: O(n)
    Auxiliary Space: O(256) i.e. O(1), As constant space is used

    :param text:
    :param anotherText:
    :return boolean:
    """
    text = removeNonAlphaNumeric(text)
    anotherText = removeNonAlphaNumeric(anotherText)

    if not equalLength(text, anotherText):
        return False

    numOfChars = 256
    charCount = [0] * numOfChars

    for i in range(len(text)):
        charCount[ord(text[i]) - ord('a')] += 1
        charCount[ord(anotherText[i]) - ord('a')] -= 1

    if any(charCount):
        return False

    return True


def anagramUsingHashMaps(text, anotherText):
    """
    The idea is a modification of the above approach where instead of creating an array of 256 characters HashMap is
    used to store characters and count of characters in HashMap. Idea is to put all characters of one String in
    HashMap and reduce them as they are encountered while looping over other the string.

    Time Complexity: O(N)
    Auxiliary Space: O(1), constant space is used

    :param text:
    :param anotherText:
    :return boolean:
    """
    text = removeNonAlphaNumeric(text)
    anotherText = removeNonAlphaNumeric(anotherText)

    if not equalLength(text, anotherText):
        return False

    map = {}

    for i in range(len(text)):
        if text[i] in map:
            map[text[i]] += 1
        else:
            map[text[i]] = 1

    for i in range(len(anotherText)):
        if anotherText[i] in map:
            map[anotherText[i]] -= 1
        else:
            return False

    if any(map.values()):
        return False

    return True



s1 = "public rel!@#$%^&&ations"
s2 = "crap built on alies."

print('Check anagram using : {0:3s}; Result is : {1:3s}'.format("anagram", str(anagram(s1,
                                                                                       s2))))

print('Check anagram using : {0:3s}; Result is : {1:3s}'.format("anagramUsingCharCount", str(anagramUsingCharCount(s1,
                                                                                                                   s2))))

print('Check anagram using : {0:3s}; Result is : {1:3s}'.format("anagramUsingCharCount", str(anagramUsingCharCount(s1,
                                                                                                                   s2))))
