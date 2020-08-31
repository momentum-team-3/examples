"""
Another crack at mystery word, but with classes.
"""
from random import choice
from math import inf


class GameState:
    """ Represents an in-progress game.
    """
    DIFFICULTY_MAP = {"easy": (4, 6), "normal": (6, 8), "hard": (8, inf)}
    MAX_WRONG_GUESSES = 8

    def __init__(self, fname):
        self.wrong_guesses = 0
        self.guesses = []
        self.word = self.get_random_word(fname)
        self._game_won = False
        self._game_lost = False

    @classmethod
    def get_random_word(cls, fname: str) -> str:
        # Get a difficulty level from the user and use it to select a random word
        while True:
            u_input = input("Select difficulty ('easy', 'normal', or 'hard'): ")
            l_input = u_input.lower()

            if l_input in cls.DIFFICULTY_MAP:
                low, high = cls.DIFFICULTY_MAP[l_input]
                break

            else:
                print("Invalid difficulty. Make another selection.")

        # endwhile

        lines_from_file = []

        with open(fname, "rt") as infile:
            for line in infile:
                line_to_keep = line.strip("\n")

                if low <= len(line_to_keep) <= high:
                    lines_from_file.append(line_to_keep)

            # end for
        # end with

        return choice(lines_from_file)

    def get_guess(self):
        # prompt user for guess until they make a valid choice
        while True:
            u_input = input("Guess a letter: ")
            l_input = u_input.lower()

            if not l_input.isalpha():
               print("Guess must be a letter. Make another selection.")

            elif len(l_input) > 1:
                print("Guess must be a single letter. Make another selection.")

            elif l_input in self.guesses:
                print("You already guessed that letter. Make another selection.")

            else:
                self.guesses.append(l_input)
                self.check_last_guess()
                return

    def check_last_guess(self):
        # check the most recent guess against the content of word
        if self.guesses[-1] in self.word:
            return True

        else:
            self.wrong_guesses += 1
            return False

    def game_won(self):
        # Update and return game win state
        for l in self.word:
            if l not in self.guesses:
                return False

        self._game_won = True

        return True

    def game_lost(self):
        # Update and return game loss state
        self._game_lost = self.wrong_guesses < self.MAX_WRONG_GUESSES
        return self._game_lost

    def get_current_visible_word(self):
        occulted_word = self.word

        for letter in self.word:
            if letter not in self.guesses:
                occulted_word.replace(letter, "_")

        return " ".join(occulted_word)

    def show_game_progress(self):
        # Report game progress to user
        remaining = self.MAX_WRONG_GUESSES - self.wrong_guesses
        current_state = self.get_current_visible_word()
        print(f"You have {remaining} turns remaining.")
        print(f"Progress: {current_state}")

    def run_game(self):
        # Print starting message
        print(f"Word chosen. Your word has {len(self.word)} letters.")
        print("Game starting.")

        # Enter main game loop
        while not (self.game_won() or self.game_lost()):
            # Get a letter from the user and add it to all_letters_guesssed
            self.get_guess()

            if self.check_last_guess():
                print("Correct!")

            else:
                print("Incorrect!")

        # endwhile
        if self._game_won:
            print("You won!")
            print(f"You guessed {self.word} in {len(self.guesses)} tries!")

        else:
            print("You lost!")
            print(f"Your word was {self.word}.")

    @staticmethod
    def play_again():
        while True:
            u_input = input("Play again (yes/no): ")
            l_input = u_input.lower()

            if l_input == "yes":
                return True

            elif l_input == "no":
                return False

            else:
                print("Ivalid choice. Make another selection.")


if __name__ == "__main__":
    print("Welcome to mystery word!")
    playing = True

    while playing:
        game = GameState("words.txt")
        game.run_game()
        playing = GameState.play_again()

    print("Goodbye!")
