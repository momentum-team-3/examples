from wf_util import read_words_from_file, make_all_lower, filter_punctuation, remove_stop_words, count_words, get_word_frequency_string


def get_word_freq_output(fname):
    """Attempt to read the frequency of the normalized words in a file. Return a formatted output
    string and an exit status. 

    If everything was okay and we were able to read (and count) all the
    words in the file, the exit status should be 0 and the output string should be a printable
    representation of the words in the file, along with their counts. If there was a problem,
    the exit status should be 1 and the output string should be an informative error message.
    
    The steps in this program are laid out below:
        * Attempt to read a list of words from the given file
            - If reading the file fails (an exception is raised), return the exception message
              and a status of 1
        * otherwise:
            - remove punctuation
            - normalize all words to lowercasem
            - remove "stop words" -- words used so frequently they are ignored
            - go through the file word by word and keep a count of how often each word is used
            - build a formatted output string with each word and its frequency in the file on
              one line
            - return the output string and a status of 0
    """
    try:
        words = read_words_from_file(fname)  # read a list of words from the file

    except FileNotFoundError as e:
        return (1, str(e))

    else:
        downcased = make_all_lower(words)  # transform all of the words to lower case
        punct_filtered = filter_punctuation(downcased)  # remove punctuation
        word_filtered = remove_stop_words(punct_filtered)  # remove the stop words
        word_counts = count_words(word_filtered)  # get a count of all the words in the file
        pretty_word_frequency = get_word_frequency_string(word_counts)  # print formatted
        return  (0, pretty_word_frequency)  # all done!

    
if __name__ == "__main__":
    import sys

    fname = sys.argv[1]
    status, output_string = get_word_freq_output(fname)
    print(output_string)
    exit(status)
