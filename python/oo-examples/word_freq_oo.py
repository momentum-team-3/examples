from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(self.filename, "rt") as infile:
            return infile.read()


class WordList:
    def __init__(self, text):
        # initialize list_of_words attribute
        self.text = text
        self.list_of_words = None

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        
        self.list_of_words = self.text.lower().replace('.', ' ').replace(',',' ').replace('!', '').split()

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        list_with_stop_words_removed = []

        for word in self.list_of_words:
            if word not in STOP_WORDS:
                list_with_stop_words_removed.append(word)       

        self.list_of_words = list_with_stop_words_removed

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        # or: return Counter(self.list_of_words)
        # create an empty dictionary
        frequencies = {}

        for word in self.list_of_words:
            if word in frequencies:
                # add 1 to the count
                frequencies[word] = frequencies[word] + 1

            else:
                # set the count for this word to 1 in the dictionary frequencies
                frequencies[word] = 1

        return frequencies


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def get_format_width(self):
        # get the width of the word field
        pass

    def get_formatted_word_with_freq(self, word):
        # Take a word in self.freqs and return a formatted string of the form '<word> | <count> ***<count-times>'
        pass

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        raise NotImplementedError("FreqPrinter.print_freqs")


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()

    else:
        print(f"{file} does not exist!")
        sys.exit(1)
