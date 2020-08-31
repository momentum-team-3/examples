from string import punctuation
""""Helper functions for the word frequency project."""


def read_words_from_file(fname: str) -> list:
    """Try to open the file named <fname>, read its contents, and return a list of the file's contents broken up by word.
    If the file doesn't exist, raise a FileNotFoundError with an informative message.
    """
    try:
        with open(fname) as file1:
            readfile = file1.read()
            wordsinfile = readfile.split()
            return wordsinfile
        
    except FileNotFoundError:
        raise FileNotFoundError(f"No file named {fname}.")


def make_all_lower(wordlist: list) -> list:
    """Take a list of strings (each string is one word) and return a new list created by downcasing all of the words in the input.
    """
    output = []
    for word in wordlist:
        lowered = word.lower()
        output.append(lowered)

    return output


def filter_punctuation_helper(word: str) -> str:
    """Remove punctuation from a single string.
    """
    temp = []
    for char in word:
        if char not in punctuation:
            temp.append(char)

    return "".join(temp)


def filter_punctuation(wordlist: list) -> list:
    """Take a list of strings and return a new list created by removing all punctuation characters from the input list.
    """
    cleanedlist = []
    for word in wordlist:
        cleanedlist.append(filter_punctuation_helper(word))
    
    return cleanedlist


def remove_stop_words(wordlist: list) -> list: 
    """Take a list of words and return a new list created by removing all 'stop words' from the input list."""
    stop_words = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
    ]
    finallist = []  # Hold all the words we want to keep.
    for word in wordlist:  # loop through every word in the output.
        if word not in stop_words:
                finallist.append(word)
    return finallist
    

# finallist = [word for word in wordlist if word not in stop_words]


def count_words(wordlist: list) -> dict:
    """"Take a list of words and return a dictionary whose keys are all the unique words in the wordlist and whose values
    are the number of times that word appeared in the list."""
    wOrDfReAk = dict()
    for word in wordlist:
        if word not in wOrDfReAk:  # wOrDfReAk = wordfreq = word frequency
            wOrDfReAk[word] = 1  # create a new entry and set its value to 1
        else:
            wOrDfReAk[word] += 1  # add 1 to the value of the existing entry

    return wOrDfReAk


def get_word_frequency_string(wordcounts: dict) -> str:
    """Take a dictionary whose keys are words and whose values are the frequency of that word in some body of text and return
    a string describing each word and its frequency each key/value pair should be formatted as below:
    
        'The word <key> appeared <value> times.'

    followed by a newline.
    """ 
    outputlines = []  # create a list to hold the lines of the output
    for wordcount in wordcounts:  # loop through the keys in the input dict
        line = f"The word {wordcount} appeared {wordcounts[wordcount]} times."
        outputlines.append(line)

    outputstring = "\n".join(outputlines)
    return outputstring


if __name__ == "__main__":
    print("Testing read_words_from_file:")
    wordlist = read_words_from_file("an-example-text-file.txt")
    print(wordlist, end="\n\n")
    print("Testing make_all_lower:")
    lower = make_all_lower(wordlist)
    print(lower, end="\n\n")
    print("Testing filter_punctuation:")
    filtered = filter_punctuation(lower)
    print(filtered, end="\n\n")
    print("Testing remove_stop_words:")
    filtered_again = remove_stop_words(filtered)
    print(filtered_again, end="\n\n")