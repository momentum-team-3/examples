"""
Another crack at mystery word.
"""
from random import choice
from math import inf


# SECTION 1: GENERAL HELPERS
def read_file_as_list(fname: str) -> list:
    """ Read the words of the file into a list.
        
            1) create an empty list to hold lines
            2) open the file for reading (use a with block)
            3) iterate through the lines of the file:
                a. strip the trailing newline character from the line
                b. add the stripped line to the list of lines
            4) return the list of lines
    """
    lines_from_file = []

    with open(fname, "rt") as infile:
        for line in infile:
            line_to_keep = line.strip("\n")

            lines_from_file.append(line_to_keep)
        # end for
    # end with

    return lines_from_file


def filter_by_length(list_of_strings: list, low: int, high: int) -> list:
    """ Return a list of the strings in list_of_strings whose
        length is no less than low and no greater than high.
    """
    filtered_by_length = [word for word in list_of_strings if low <= len(word) <= high]
    return filtered_by_length


def random_selection(collection: list):
    """ Apply random.choice to collection."""
    return choice(collection)

    
def get_difficulty():
    while True:
        u_input = input("Guess a letter: ")
        l_input = u_input.lower()

        if l_input == "easy" or l_input == "normal" or l_input == "hard":
            return l_input

        else:
            print("Invalid difficulty. Please select again.")


def get_guess(letters_guessed):
        while True:
                u_input = input("Guess a letter: ")
                l_input = u_input.lower()

                if not l_input.isalpha():
                        print("Guess must be a letter. Make another selection.")

                elif len(l_input) > 1:
                        print("Guess must be a single letter. Make another selection.")

                elif l_input in letters_guessed:
                        print("You already guessed that letter. Make another selection.")

                else:
                        return l_input




def get_play_again():
        """ Check if the user wants to play again.
        """
        while True:
                u_input = input("Play again (YES/NO): ")
                l_input = u_input.lower()

                if l_input == "no":
                        return False

                elif l_input == "yes":
                        return True

                else:
                        print("Invalid option. Make another selection.")


def get_word_to_guess(difficulty):
        # difficulty is the difficulty supplied by the user and returned from get_difficulty()
        words = read_file_as_list("words.txt")
        # convert difficulty to upper and lower bound for word lengths
        if difficulty == "easy":
                lower = 4
                upper = 6

        elif difficulty == "normal":
                lower = 6
                upper = 8

        else:  # input validation ensured that easy is equal to either 'easy', 'normal', or 'hard', else assumes easy == 'hard' 
                lower = 8
                upper = inf
        
        words_to_choose = filter_by_length(words, lower, upper)
        word = random_selection(words_to_choose)

        return word


def check_guess(letter_guessed, word_to_guess):
        # Check for membership in word
        return letter_guessed in word_to_guess


def check_victory(letters_guessed, word_to_guess):
        # Check whether all unique letters have been guessed
        for letter in word_to_guess:
                if letter not in letters_guessed:
                        return False

        return True


def string_with_hidden(letters_guessed, word):
        """ Replace letters that have not been guessed
            with an underscore and separate the resulting
            string with spaces.
        """
        occulted_word = word
        
        for letter in word:
                if letter not in letters_guessed:
                        # Hide the letter if the player hasn't guessed it
                        occulted_word.replace(letter, "_") 

        return " ".join(occulted_word)


# SECTION 3: MAIN LOOP
def game_loop(is_first_game):
    if is_first_game:
        print("Welcome to mystery word!")


    # Set up game state
    difficulty = get_difficulty()
    word = get_word_to_guess(difficulty)
    wrong_guesses = 0
    max_wrong_guesses = 8
    letters_guessed = []

    # Print starting message
    print(f"Word chosen. Your word has {len(word)} letters.")
    print("Game starting.")

    # Enter main game loop
    while wrong_guesses < max_wrong_guesses:
        if check_victory(letters_guessed, word):
            print("You win!")
            print(f"You guessed {word} in {len(letters_guessed)} tries!")

            if get_play_again():
                return game_loop(False)

            else:
                print("Goodbye!")
                exit(0)

        else:
            # Report game progress to user
            print(f"You have {max_wrong_guesses - wrong_guesses} turns remaining.")
            print(f"Progress: {string_with_hidden(letters_guessed, word)}")

            # Get a letter from the user and add it to all_letters_guesssed
            guess = get_guess(letters_guessed)

            letters_guessed.append(guess)

            if check_guess(guess, word):
                print("Correct!")

            else:
                print("Incorrect!")
                wrong_guesses += 1

    # endwhile
    # assert wrong_guesses == max_wrong_guesses

    print("You lost!")
    print(f"Your word was {word}!")

    if get_play_again():
        return game_loop(False)

    else:
        print("Goodbye!")
        exit(0)


if __name__ == "__main__":
    game_loop(True)
