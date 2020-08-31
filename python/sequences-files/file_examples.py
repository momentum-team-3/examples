# Files are external resources that we can interact with to send and read data (these kinds of
# resources are often lumped together under the label "IO"). Python makes handling files very
# easy. Files can contain either text or binary data, but we'll be working exclusively with
# text files for now.


def file_basic_examples():
    # We can open a file with the 'open' function, as seen below. The open function has a lot of
    # optional arguments, but let's start with the basics. Calling open with just a file path
    # opens that file for reading.
    try:
        infile = open("an-example-text-file.txt")

    except FileNotFoundError:
        print("That's not a file!")

    else:
        print("Whew, that was a close one!")

    input("press any key when you're ready to continue")

    # We put that in a try block because it would have thrown an error 
    # let's see what happens when we try to open a file that doesn't exist
    try:
        infile2 = open("not-a-real-file.txt")

    except FileNotFoundError:
        print("I told you this wouldn't work!")

    else:
        print("I would be really surprised if this message was printed.")
        infile2.close()

    input("press any key when you're ready to continue")

    # The simplest way to read data from a file is with the read method.
    words = infile.read()
    print("file contents:\n", words)

    # It's important to make sure that we close files when we're done with them!
    # luckily, this won't be much of a problem for us if we're using with/as to manage
    # our files.
    infile.close()


def with_as_examples():
    # Especially in more complex projects, it can become difficult to ensure that our
    # files are properly closed even when the program exits with an exception. That's
    # why we almost always want to open files using the with keyword. Proper usage is
    # illustrated below.
    print("Demonstrating usage of with/as")

    # the syntax of with is the with keyword, followed by a call to the open function,
    # followed by the as keyword, followed by a variable name of our choosing. Within
    # the with block, we can manipulate and interact with that file using the variable
    # name that appears after the as keyword. After the with block, the file will not
    # be freely accessible.
    with open("an-example-text-file.txt") as infile:
        words = infile.read()
        print("file contents (opened using 'with'):\n", words)

    input("press any key when you're ready to continue")

    # What makes 'with' so great is that no matter how we exited the with block (returning from
    # a function, encountering an exception, etc.) 'with' will make sure that the file is
    # closed properly. This completely eliminates an entire dimension of programming errors.


def file_iteration_examples():
    # Files are sequences and we can iterate through text files using a for loop. The following
    # should produce roughly the same output as above
    with open("an-example-text-file.txt") as infile:
        print("file contents (shown with iteration):\n")

        for line in infile:
            print(line)

    # Being able to use a file in a for loop winds up eliminating even more sources of bugs,
    # and is a very convenient way to work with files.


def writing_and_file_modes():
    # So far we've seen how to read from a file, but how do we write to one?
    # Files have a mode, which determines what you're allowed to do with the opened file.
    # By default, the mode is 'r', short for 'read', meaning that we can read data from the
    # file. There's also 'w', short for 'write' (write to file, overwriting any existing data),
    # and 'a', short for 'append' (add new data to the end of the file).

    # If we want to create a file that doesn't exist, we can open it using 'w+' as the mode.
    # the '+' option means 'create this file if it doesn't exist', and it can be used with
    # many different file modes (for a full description of file modes, see
    # https://docs.python.org/3/library/functions.html#open).

    # In the example below we're putting a lot of things together. The end result is that we'll
    # create an output file named 'an-example-output-file.txt' and write every other line
    # from our input file to that output file.

    with open("an-example-text-file.txt", "r") as infile:
        with open("an-example-output-file.txt", "w+") as outfile:
            linecount = 0
            for line in infile:
                linecount += 1
                if linecount % 2 == 1:
                    print("line", linecount, "was added to the output file")
                    # We use the 'write' method to write data to an output file
                    # to preserve the line structure of the original, we use an f-string
                    # to add a newline character to the end of the line
                    outfile.write(f"{line}\n")

    print("Success!")


if __name__ == "__main__":
    writing_and_file_modes()