"""This application should do the following until the user enters the string 'quit':

    1) print a list of acceptable commands ('add', 'help', 'quit')
    2) get a command from the user
    3) if the command is 'add':
        a) read a number from the command line and convert it to an integer
        b) read another number from the command line and convert it to an integer
        c) add the result together and show it to the user

    4) if the command is 'help':
        a) reprint the list of acceptable commands
        b) go back to the top of the loop

    5) if the command is 'quit':
        a) exit the program

    6) if an error occurs:
        a) print a message saying the input couldn't be handled.
        b) go to the top of the loop
"""

def main():
    print("enter one of the following: 'add', 'help', or 'quit'")
    while True:
        # implement step one here
        command = input("command: ")
        try:
            if command == 'add':
                num1 = int(input("num1: "))
                num2 = int(input("num2: "))
                print("sum: ", num1 + num2)

            elif command == 'help':
                print("enter one of the following: 'add', 'help', or 'quit'")

            elif command == 'quit':
                break

            else:
                print("I don't recognize the command ", command)

        except Exception:
            print("Couldn't handle input.")

    print("goodbye!")
    return


if __name__ == "__main__":
    main()