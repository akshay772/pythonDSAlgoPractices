def splitWordsFromTextRecursive(text, referenceOfWords, output=None):
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []

    # For every word in list
    for word in referenceOfWords:
        # If the current phrase begins with the word, we have a split point!
        if text.startswith(word):
            # Add the word to the output
            output.append(word)

            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return splitWordsFromTextRecursive(text[len(word):], referenceOfWords, output)

    # Finally return output if no phrase.startswith(word) returns True
    return output


def splitWordsFromText(text, referenceOfWords):
    result = []

    for ele in referenceOfWords:
        if ele in text:
            result.append(ele)
            text = text.replace(ele, '')

    if text == '':
        return result
    else:
        return []


print(splitWordsFromTextRecursive('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
print(splitWordsFromTextRecursive('themanran', ['the', 'ran', 'man']))
print(splitWordsFromText('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
