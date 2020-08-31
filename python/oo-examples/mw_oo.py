from math import inf
from random import choice


class SecretWord:
    """ Represents a word to be guessed. This class handles all of the state
        needed to keep track of what has been guessed and what needs to be guessed.
    """
    def __init__(self, word):
        self.word = word
        self.letters_guessed = []
        self.guessed = False

    def add_guess(self, letter):
        if letter in self.letters_guessed:
            raise ValueError("Already guessed.")

        self.letters_guessed.append(letter)

    def check_last_guess(self):
        # Determine if the last guess was correct
        return self.letters_guessed[-1] in self.word

    def check_word_guessed(self):
        # Determine if the word has been successfully guessed
        for letter in self.word:
            if letter not in self.letters_guessed:
                return False

        return True

    @property
    def guesses(self):
        # Get the user's guesses up to now as a string
        return ", ".join(self.letters_guessed)

    def __str__(self):
        # Print only the
        output = []

        for c in self.word:
            if c in self.letters_guessed:
                output.append(c)

            else:
                output.append("_")

        return " ".join(output)


class GameState:
    """ Holds the data and methods needed to run a
        game of mystery word. While the SecretWord class
        is responsible for keeping track of what has been
        guessed, GameState manages the game setup, user interaction,
        and checking for game win/loss.
    """
    # class constants
    MAX_WRONG_GUESSES = 8

    DIFFICULTY_MAP = {
        "easy": (4,6),
        "normal":(6,8),
        "hard":(8, inf)}

    WORDS_FILE = "words.txt"

    def __init__(self):
        self.wrong_guesses = 0
        self.secret_word = None

    @property
    def turns_left(self):
        # Calculate the number of turns remaining based on self.wrong_guesses and MAX_WRONG_GUESSES
        return self.MAX_WRONG_GUESSES - self.wrong_guesses

    def setup_game(self):
        """ Get desired difficulty from user and select.
            an appropriate secret word.
        """
        # Get difficulty and select lower and upper length
        # bounds
        d = self.get_difficulty()
        low, high = self.DIFFICULTY_MAP[d]

        with open(self.WORDS_FILE) as i_f:
            words = [w.strip() for w in i_f if low <= len(w.strip()) <= high]

        self.secret_word = choice(words)

    def get_difficulty(self):
        # Prompt a user to submit difficulty until they make a valid selection
        while True:
            u_input = input("Select a difficulty ('easy', 'medium', or 'hard'): ")
            l_input = u_input.lower()

            if l_input in self.DIFFICULTY_MAP:
                return l_input

            else:
                print("Invalid difficulty. Make another selection.")

    def get_guess(self):
        # Prompt a user to submit difficulty until they make a valid selection
        while True:
            u_input = input("guess a letter: ")
            l_input = u_input.lower()

            try:
                self.secret_word.add_guess(l_input)
                return

            except ValueError:
                print("Letter already guessed. Make another selection.")

    def get_play_again(self):
        # Prompt a user whether they want to play again
        while True:
            u_input = input("play again? (yes/no): ")
            l_input = u_input.lower()

            if l_input == "yes":
                return True

            elif l_input == "no":
                return False

            else:
                print("Unrecognized option. Make another selection.")

    def play_turn(self):
        # Runs a single turn in the game
        print(f"{self.turns_left} turns remaining.")
        print(f"Guessed so far: {self.secret_word}")
        self.get_guess()

        if self.secret_word.check_last_guess():
            print("Correct!")

        else:
            print("Incorrect!")
            self.wrong_guesses += 1

    def play_game(self):
        # Main game loop

        # Initialize the game
        self.setup_game()

        print(f"Mystery word selected. Myster word has {len(self.secret_word)} letters.")

        while self.turns_left > 0:
            self.play_turn()

            if self.secret_word.check_word_guessed():
                print("You win!")
                print(f"You guessed {self.secret_word.word} in {len(self.secret_word.letters_guessed)} turns!")

                if self.get_play_again():
                    self.play_game()

                else:
                    print("Goodbye!")
                    exit(0)


if __name__ == "__main__":
    print("Welcome to mystery word!")

    Game = GameState()

    Game.play_game()