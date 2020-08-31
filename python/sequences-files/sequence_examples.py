import sys


def lineref():
    """Helper for printing line numbers (students, ignore this)."""
    return f"(see line {sys._getframe(1).f_lineno})"

# A collection is a structured group of data. Intuitively, you can think of a collection as
# "anything that can be used with a for loop".
#
# A sequence is an *ordered* collection -- it has a first element, a second element, and so on.
# Python includes three fundamental sequence types: lists, tuples, and strings.
#
# In addition to these three types, Python provides an unordered collection type that
# allows us to associate keys with values. These collections are called dictionaries.
#
# We'll examine these four types below, then dive into increasingly sophisticated aspects of 
# working with sequences. You do *not* need to know everything covered in this reference to
# complete your assignments in this phase. This is intended as a reference and guide you
# can come back to repeatedly, developing your understanding a little further each time.
#
# Let's get started!
# 
# lists are exactly like JavaScript arrays; they even look alike! They also support a lot of
# similar methods and operations.
LISTX = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# tuples are like lists, but they're immutable, meaning elements can't be added, removed, or
# changed. Tuples are used internally by Python for a lot of purposes, so we need to know
# how to work with them, but for everyday purposes lists are more useful.
TUPLEX = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

# strings work are very similar to JavaScript strings. They can be indexed with numbers just
# like lists can. Like tuples, strings are immutable.
STRINGX = "This is a great class!"

# dictionaries are sort of like lists, but instead of accessing items by its order in the
# sequence, you access items in dictionaries by a "key". The entries of dictionaries are
# called key-value pairs for this reason. They're sort of like JavaScript object literals
# in appearance and everyday applications, but there are important differences. Not all Python
# objects can be used as dictionary keys. As a rule of thumb, only immutable objects can
# be used as keys. Strings are probably the most common type of dictionary key.
DICTX = {"Shane": "good student", "Kyle": "good student", "Tori": "good student"}


# Each of the example functions below demonstrates some aspect of working with python sequences
# You can run this file from the command line with an appropriate argument to see the output of
# each function, or you can import this module from the command line and play around
# with the values defined above.

def index_examples():
    # "indexing" means accessing an item in a sequence by a key. For sequences
    # (lists, tuples, and strings), this key is just its position in the sequence
    # (remember that the first element has index 0). To index an element, put a pair
    # of square brackets after the sequence you're indexing, and inside those brackets
    # put the key for the element you want to access.
    x = LISTX[0]

    # What will be printed to the command line?
    print("The 1st element of LISTX is", x, lineref())

    y = TUPLEX[1]

    # What will be printed to the command line?
    print("The 2nd element of TUPLEX is", y, lineref())

    z = STRINGX[2]

    # What will be printed to the command line?
    print("The 3rd element of STRINGX is", z, lineref())

    # Sequences can be indexed starting from the last element using negative numbers! The
    # index -1 will get the last element of the sequence regardless of its length, -2 will
    # get the second-to-last, and so on. This will become even more useful once we've learned
    # about slicing (later this week).

    w = STRINGX[-1]

    # What will be printed to the command line?
    print("The last element of STRINGX is", w, lineref())

    # indexing a dictionary works just the same as indexing a sequence, but its key isn't
    # based on order. Instead, we supply the dictionary with explicit keys (an order is sort
    # of like an implicit key) and we tell it what values to associate with those keys.
    u = DICTX["Shane"]

    # What will be printed to the command line?
    print("The value of the key 'Shane' in DICTX is", u, lineref())

    # If a collection is mutable, you can use indexing in combination with assignment
    # to change the value for that key in the sequence.
    LISTX[0] = -1

    # What is the value of LISTX now? What is its first element?
    print("The list LISTX is now", LISTX, lineref())

    # You can do the same with dictionaries!
    DICTX["Shane"] = "BAD student"

    # What is the value of DICTX now? What is the value associated with the key 'Shane'?
    print("The dict DICTX is now", DICTX, lineref())

    # If you assign to a key that the the dictionary doesn't contain, that key will be
    # added to the dictionary.
    DICTX["Jon"] = "good student"

    # What is the value of DICTX now? What keys does it contain?
    print("The dict DICTX is now", DICTX, lineref())

    # However, if you try to reference the value of a key that doesn't exist, it will throw
    # an error!
    try:
        mistake = DICTX["Will"]

        # Will this print?
        print("The value of mistake is", mistake, lineref())

    except KeyError:
        # Will this print?
        print("That was a foolish thing to try to do!", lineref())

    # That's it for indexing basics!


def basic_sequence_functions():
    # Python provides several functions that work with most sequences. Using these in conj-
    # unction with other Python tools will dramatically extend their utility, so we're
    # going to start by looking at 2 functions and 1 category of functions.
    #
    # 1.                  constructors
    # 'constructors' are what we call the functions that create values of a certain type.
    # in Python, you call a type's constructor by using the type's name like it's a function.
    # the 'list' constructor is especially handy: it takes the elements in a sequence and
    # produces a list with the same elements. This will be useful for transforming sequences
    # into a form that's simple to work with.

    # in this example, 'list(STRINGX)' will produce a list whose elements are the individual
    # characters in the string 'STRINGX'
    lsx = list(STRINGX)

    # What will be printed to the command line?
    print("The value of lsx is", lsx, lineref())
    
    # 2.                  the len function
    #
    # 'len' is short for 'length', and the 'len' function does exactly what you would
    # expect it to: it returns the number of elements in the sequence. It can be used with
    # most collections that can be indexed.

    l = len(TUPLEX)
    # What will be printed to the command line?
    print("There are", l, "elements in TUPLEX")

    # 3.                 the range function
    #
    # the 'range' function takes a number (which we'll call x) as an argument and
    # produces a sequence of all the numbers from 0 to x - 1. It can be used in conjunction
    # with 'len' to get a sequence of the indices of a sequence. 'range' can also be used with
    # more than one argument, but most commonly it's used with just one (though you'll see an
    # an example of using range with 2 arguments later in this file; see if you can figure out
    # what it does!)

    # This will produce a list of all the indices in the list LISTX
    li = list(range(len(LISTX)))

    # What is the value of li?
    print("The value of li is", li, lineref())


def for_loop_basics():
    # you can loop through the values one-by-one in Python using a for loop. A for loop
    # has the following form:
    #
    #    for <loop-variable> in <sequence>:
    #        <statment-1>
    #            .
    #            .
    #            .
    #       <statement-n>
    #
    # <sequence> is a list, tuple, string, dictionary, or other collection of data
    # (in python, things that can be used in a for loop are called "iterables")
    #
    # <loop-variable> is a variable whose values will be taken one at a time from the
    # items in <sequence>. The first time the for loop block runs, the value of
    # <loop-variable> will be the first item in <sequence>. The second time the loop
    # block runs, the value of <loop-variable> will be the second item in <sequence>.
    #
    # <statement-1> ... <statement-n> can be any Python statements. There must be at least
    # one statement in the for loop block.

    # What will be printed to the terminal?
    print("Printing the elements of STRINGX using a for loop", lineref())
    for c in STRINGX:
        print(c)

    # if you want to loop over the indices of something, you can use 'range' and 'len' in
    # a for loop, like this:
    print("Printing the elements of LISTX by looping through its indices", lineref())
    for i in range(len(LISTX)):
        x = LISTX[i]
        print(x)

    # This can be useful if you need to modify the elements in an array, or access elements
    # from different arrays.
    print("Resetting the value of LISTX using for and range", lineref())
    for i in range(len(LISTX)):
        LISTX[i] = i + 1

    # This isn't the best way to do this -- the Python documentation specifically
    # suggests you should use other methods -- but it's very common, and it's the
    # easiest way to understand. If this makes more sense to you, you should use it
    # until you feel more comfortable with sequences and iterables!

    # that's it with for loop basics!


def membership_tests():
    # Besides being used in a for loop statement, the 'in' keyword is used to test whether
    # a Python object is equal to an element in a sequence. It works like this:
    #
    #     <thing> in <sequence>
    #
    # and it evaluates to either True or False.
    # exactly what it means for <thing> to be a member of <sequence> depends on the type
    # of the sequence.

    # for lists and tuples, 'in' will test if the left-hand expression is an element in
    # the list or tuple. It's pretty straightforward!

    # which will be printed?
    if 1 in LISTX:
        print("The number 1 IS in LISTX", lineref())

    else:
        print("The number 1 IS NOT in LISTX", lineref())


    # which will be printed?
    if 1 in TUPLEX:
        print("The number 1 IS in TUPLEX", lineref())

    else:
        print("The number 1 IS NOT in TUPLEX", lineref())

    # for dictionaries, <thing> in <dict> will test whether the element 'thing' is a
    # key in the dictionary 'dict'. This is usually what we're more interested in.

    # which will be printed?
    if "Shane" in DICTX:
        print("'Shane' IS a key in DICTX", lineref())

    else:
        print("'Shane' is NOT a key in DICTX", lineref())

    # which will be printed (remember that 'in' will tell us whether "good student" is among
    # the dictionarie's keys)
    if "good student" in DICTX:
        print("'good student' IS a key in DICTX", lineref())

    else:
        print("Shane is NOT a key in DICTX", lineref())

    # for strings, <thing> in <string> will tell you whether <thing> is a substring of <string>.
    # (string A is a substring of string B if an uninterrupted sequence of characters within
    # string B is exactly equal to string A).

    # Which will be printed?
    if "a" in "Shane":
        print("One of the letters in 'Shane' is 'a'", lineref())

    else:
        print("One of the letters in 'Shane' is NOT 'a'", lineref())

    # Which will be printed?
    if "ne" in "Shane":
        print("The string 'ne' is a substring of 'Shane'", lineref())

    else:
        print("The string 'ne' is NOT a substring of 'Shane'", lineref())

    # That's all we need to know about membership tests for now!


def slicing_examples():
    # You may remember the Array and String slice method from JavaScript. We didn't use
    # it much, mostly to produce a copy of an array. Python has a dedicated slicing syntax,
    # and it's extremely useful. The slicing syntax is based on the indexing syntax, but with
    # ':' separating the starting index, the stoping index, and the step amount.
    # There are a few different forms of slice, and it's easiest to see how they work
    # through examples.

    # First, I'm going to need a big list to demonstrate all the things I can do with slicing.
    ls = list(range(100))

    # And I might as well have a big tuple too!
    tup = tuple(range(100, 200))
    
    # And a big string, since slicing works with strings
    st = ""

    for code in range(32, 127):
        st += chr(code)

    # The simplest way to use slicing is to get everything from a certain index in a sequence
    # to the end.
    lsx = ls[49:]

    # What will this print?
    print("The value of lsx is", lsx, lineref())

    # You can also do it the other way around, using slicing to get everything from the start
    # of a string up to a certain index.
    tupx = tup[:49]

    # What will this print?
    print("The value of tupx is", tupx, lineref())

    # Or you can include a starting index and a stopping index to take a chunk out of the middle
    stx = st[10:90]

    # What will this print?
    print("The value of stx is", stx, lineref())

    # You can use negative indices in slices! If I wanted everything except the first 10 and
    # last 10 elements of the string st, I could just do the following.
    sty = st[10:-10]

    # What will this print?
    print("The value of sty is", sty, lineref())
    
    # Slicing a sequence produces a totally new sequence, so modifying a sliced sequence won't
    # affect the original

    lsy = ls[:49]
    lsy[0] = -1

    if ls[0] == -1:
        raise Exception("Oh no, we modified the original array!")

    else:
        print("We will only see this message if changing lsy didn't change ls", lineref())

    # This feature of slicing is often exploited to create copies of a sequence
    lsz = ls[:]  # this is a slice of the whole array, so it's just a copy of the original!

    # What will this print?
    print("The value of lsz is", lsz, lineref())

    # a slice can take an additional argument, a 'step', which will skip over elements
    # in the sequence you're slicing
    tupy = tup[20:40:2]  # this will produce a tuple from every 2nd element between indices
                         # 20 and 40 in tup

    # What will this print?
    print("The value of tupy is", tupy, lineref())

    # The step argument can be used with any combination of other arguments.
    tupz = tup[::2]  # This will create a new tuple from every 2nd element of tupz

    print("The value of tupz is", tupz, lineref())

    # The step argument can also be negative, with a surprising result -- it reverses
    # the order of the values in the original sequence.
    stw = st[::-1]

    # What will this print?
    print("The value of stw is", stw, lineref())

    # A few notes on using slices:
    #
    # 1) The first element of a slice is always the element with the index of the first argument
    #    if, x, y, and z are numbers and ls is a list, the first element in ls[x:y:z] is
    #    ls[x]
    #
    # 2) The LAST element of a slice is always the element with index one less than the index
    #    of the second argument. if x, y, and z are numbers and ls is a list, the last element
    #    of ls[x:y:z] is ls[y-1]
    #
    # 3) The above notes are true for positive indices with a step of 1, but it may work a
    #    a little differently for negative indices or if the step is some other number. The
    #    best way to understand these differences, in my experience, is through experimenting
    #    in the terminal.
    #
    # 4) In general, slicing won't work with sequence types that don't have numeric indices.
    #    You can't take a slice from a dict, for example.

    # That's all we need to know about slicing for now!


def functions_for_iterating():
    # There are many functions that we can use in combination with for loops, but I want
    # to go over two especially useful builtin functions right now: zip and enumerate.
    # zip and enumerate both take sequences as arguments and produce a new sequence. They
    # are a little hard to understand at first, because they produce a special kind of sequence
    # called an 'iterator', but they dramatically extend what we can do with for loops!

    # 1.                             zip
    # 
    # The zip function takes two sequences as an argument and produces a sequence of tuples
    # if the s1 and s2 are indexable sequences, then the values of zip(s1, s2) are
    # (s1[0], s2[0]), (s1[1], s2[1]) ... (s1[n], s2[n]). I know I just kind of threw n in
    # there at the end, but it's actually a specific number: 1 less than the length of she
    # shorter sequence!
    #
    # zip makes it easy to pair up sequences. This is useful when, for example, we want
    # compare every element in one sequence to a matching element in another

    # What will this print?
    print("Example of using zip to compare corresponding elements", lineref())
    for (shc, slc) in zip("Shane", "Sloan"):
        if shc == slc:
            print("'Sloan' and 'Shane' have", shc, "in common!")

    # what's going on with 'for (shc, slc)'? This is just a way of creating multiple
    # variables when the elements of the sequence you're looping through are tuples.
    # Normally the parentheses are ommitted and this would be written as
    # 'for shc, slc in zip("Shane", "Sloan"):' but I think including the parentheses
    # makes it clearer what's going on -- the elements of zip("Shane", "Sloan") are tuples,
    # and my for loop is just using this special syntax to access the elements of those
    # tuples when assigning my loop variables.

    # 2.                             enumerate
    #
    # enumerate takes just one sequence for an argument and produces a new sequence of tuples.
    # if the argument to enumerate is a sequence 'sx', then the elements of the sequence it
    # returns are (0, sx[0]), (1, sx[1]) ... (n, sx[n]); I know I threw another random n in
    # there, but it's actually just len(sx) - 1 again!
    #
    # Enumerate is useful when you need the indices of a sequence and it's values, or even
    # just the indices of a sequence. In fact, enumerate is how the creators of Python
    # suggest you loop over the indices of a sequence. But they say a lot of things, and
    # many people find 'len(range(sx))' a more intuitive way to do it.
    print("Demonstrating enumerate", lineref())
    for (index, character) in enumerate("Shane"):
        print("the", index, "-th element of 'Shane' is", character)

    # If zip and enumerate are feeling intimidating don't worry, there's nothing they allow
    # you to do that you can't do some other way; but they make for loops much easier to write
    # and more readable, they're fun to use, and they're a good window into python's deeper
    # workings.

    # But for now, we'll move on!


def basic_sequence_operations():
    # Here we'll talk about 

    # 1. '+' and '*'
    # You can use '+' and '*' with any sequence that can be indexed by numbers.

    # '+' will take two sequences of the same type and produce a new sequence of all of the
    # elements of both. This is called 'concatenation'.
    lsx = LISTX + [22, 33, 44]
    stx = "Sloan" + "Shane"
    tupx = ("Tori", "Izis") + ("Harrison", "Robert")
    
    # What will be printed?
    print("The value of lsx is", lsx, lineref())
    print("The value of stx is", stx, lineref())
    print("The value of tupx is", tupx, lineref())

    # '*' will take a sequence, which we'll call 'sx', and a number, which we'll call 'n',
    # and produce a new sequence by concatenating n copies of sx. We don't end up using this,
    # very much, but it's actually the fastest and simplest way to create a list from repeated
    # elements. So it's very useful on the rare occassions that it's useful at all!
    lsy = LISTX * 3
    sty = "Harrison" * 4
    tupy = ("Tori") * 7

    # What will these print?
    print("The value of lsy is", lsy, lineref())
    print("The value of sty is", sty, lineref())
    print("The value of tupy is", tupy, lineref())

    # 2. '<', '>', and '=='
    # It's probably not too surprising that sequences in Python can be compared, but the
    # idea that it's sensible to ask whether [4, 5] > [1, 2, 3] may need some explanation
    # (it is sensible, and [4, 5] is indeed greater than [1, 2, 3]).
    #
    # We'll start with strings. Strings are sorted according to what we're used to calling
    # alphabetical ordering -- we start by comparing the first character in each string.
    # If the characters are different, then the order of the strings is the order of the
    # first characters. If the first characters are different, then we try again with the
    # next two. We continue this process until we find two characters that aren't equal, or
    # we reach the end of one of the strings. If we reach the end of one of the strings
    # (but not the other) before we find corresponding characters that differ, then
    # the shorter string precedes the longer. If we reach the end of both strings
    # without finding corresponding characters that differ, then the strings are exactly
    # equal.
    #
    # That's a mouthful! The good news is that it's just a detailed description of the
    # process you probably used to line up for lunch in your 3rd grade class (assuming
    # you lined up alphabetically). Really, it's exactly the same! Mathematicians call this
    # 'lexical ordering' (a phrase you definitely don't have to remember), and it can be used
    # with lots of things besides strings.
    #
    # For Python sequences, '>' and '<' indicate how items relate according to this
    # ordering rule. We'll start with a few examples for strings, which should
    # be pretty familiar, then we'll try with other kinds of sequences.
    #
    # Example 1: who goes to lunch first?
    # 's' comes before 't' in the alphabet, so 'Shane' precedes 'Tori'. 'Precedes' is basically
    # the same as 'less than'
    if "Shane" < "Tori":
        print("Shane goes to lunch first!", lineref())

    else:
        print("Tori goes to lunch first!", lineref())

    # Example 2: What about Sloan vs Shane?
    # Because Sloan and Shane have the same first letter, we'll have to compare the second lett-
    # ers to figure out who goes to lunch first. Because 'h' comes before 'l', 'Shane' precedes
    # 'Sloan', so 'Shane' is our reigning lunch champion.
    if "Shane" < "Sloan":
        print("Shane goes to lunch first!", lineref())

    else:
        print("Sloan goes to lunch first!", lineref())

    # Example 3: now let's try with lists!
    # We'll compare two lists: the list '[3, 5, 7]', and the list '[3, 5, 6]'.
    # The first element in each is the same, so we compare the second element in each.
    # Those are also the same, so we compare the third. 6 is less than 7, so the list
    # '[3, 5, 7]' is preceded by the list '[3, 5, 6]'
    if [3, 5, 7] < [3, 5, 6]:
        print("[3, 5, 7] precedes [3, 5, 6]", lineref())

    else:
        print("[3,5, 6] precedes [3, 5, 7]", lineref())

    # Example 4: try this one on your own
    # Which block will be executed, the if or the else?
    if [4, 9, 8] < [4, 9, 7, 11]:
        print(" [4, 9, 8] precedes [4, 9, 7, 11]", lineref())

    else:
        print(" [4, 9, 7, 11] precedes [4, 9, 8]", lineref())

    # Tuples work exactly like lists with respect to '<' and '>', so we won't treat them
    # separately. On to the next topic!


def basic_collection_methods():
    # Here we'll go over the bread and butter methods for three of the four types we've
    # been learning about. Tuples don't really have any interesting methods besides
    # the operators we've talked about above, so we're going to restrict ourselves
    # to looking at core methods for lists, strings, and dictionaries.
    #
    # 1. lists
    #
    # lists have five fundamental methods I'd like to talk about: append, pop, remove,
    # index, and extend. These methods either implement important list operations, or
    # (in my experience) simplify a lot of complex problems.
    #
    #                               append
    # the append method adds an element to the end of a list. Append works a lot like
    # push in JavaScript.
    LISTX.append(32)

    # What will this print?
    print("The value of LISTX is", LISTX, lineref())

    #                                pop
    # the pop method works exactly like the pop method in JavaScript. That means it does 2
    # things -- it removes the last element in the list, and returns the element that
    # was removed. 'Push' and 'pop' were named for the spring-loaded plate-holders in
    # university cafeterias in the mid-20th century -- 'pushing' a plate adds it to the
    # stack of plates, while 'popping' a plate removes it from the stack and gives you
    # a plate to put your lunch on. I find this a very helpful way to remember what
    # push (append, in Python) and pop do.
    x = LISTX.pop()

    # What will this print?
    print("The value of x is", x, lineref())

    # What will this print?
    print("The value of LISTX has been restored to", LISTX, lineref())

    #                             extend
    # extend is sort of like a super-append. It adds all of the elements of the argument
    # collection to the list that extend was called on. What's especially valuable about
    # this method is that it can be used with *any* sequence type.
    LISTX.extend(TUPLEX)

    # What will this print?
    print("The value of LISTX is now", LISTX, lineref())

    #                             remove
    # remove removes the first element matching the argument from the list the method
    # is called on. Remove will raise an exception if the list doesn't contain that
    # element, so it's a good idea to check that the argument is an element of
    # the list first (or to call it inside a try block). Let's use remove to take out
    # all of the elements we added with extend
    for x in TUPLEX:
        LISTX.remove(x)

    # What will this print?
    print("The value of LISTX has been restored to", LISTX, lineref())

    #                             index
    # index will return the index of the first occurrence of its argument
    # in the list that index was called on. So [1, 2, 3, 4].index(3) will return
    # 2, [0,1,1].index(1) will return 1, and [4,4,5,8,6].index(4) will return 0.
    # The index method will raise an exception if the argument doesn't occur
    # in the list, so it's wise to check that it exists or put the call to index
    # in a try block.
    x = LISTX.index(9)

    # What will this print?
    print("The value of x is", x, lineref())

    # 2.                       str methods
    # The string methods we'll go over here will fall into four categories: testing strings,
    # partitioning strings, transforming strings, and creating new strings. Strings probably
    # have more methods than any other builtin class, so I've tried to restrict my examples
    # to a few representative methods from each category that will be immediately useful to
    # us. You should check out the rest of the methods at the official Python documentation
    # (https://docs.python.org/3/library/stdtypes.html#textseq). There's a fifth broad category,
    # searching, that we won't go over just yet, but you can find out more about it at that
    # link.

    # 2a.                      testing strings
    #
    #                           isalpha
    # the isalpha method will test whether every character in the string is an alphabetic
    # character and return True or False depending on the result of the test.

    if "Sloan".isalpha():
        print("Sloan's name doesn't have any numbers", lineref())

    else:
        print("Sloan's name has some numbers, like Elon Musk's kid", lineref())

    #                          isdigit
    # isdigit is a lot like isalpha, but it tests whether the string is made up strictly
    # of the characters '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. isdigit is
    # so similar to isalpha that we won't bother producing another example here.

    # 2b.                      partitioning strings
    #
    #                          split
    # The split method will break a string at every occurrence of its argument (or
    # whitespace, if it's called without an argument) and return a list containing all of
    # the strings that the input was partitioned into. This is very useful for text processing,
    # eg, for breaking sentences into words.

    # What will be printed to the terminal?
    strings = "This is a perfectly fine sentence".split()

    print("Demonstrating the split method", lineref())
    for string in strings:
        print(string)

    # 2c.                   transforming
    #
    #                        lower/upper
    # the lower method will transform every character in the string to lower case. The upper
    # method will transform all the characters to upper case! Very simple! These methods are
    # most useful when you don't want to deal with case at all -- just transform everything
    # to lower case (or upper case) and carry on! We'll demonstrate lower and let you imagine
    # how upper might work.

    # What will be printed to the terminal?
    SHANE = "SHaNe".lower()

    print("Demonstrating the lower method with the name", SHANE, lineref())

    # 2d.                   building strings
    #
    #                       join
    # The join method takes a string and sequence of strings and produces a new string by
    # inserting the string that join was called on between every string in the collection.
    # let's look at an example.
    students = ["Kyle", "Tori", "Robert", "Harrison", "Kim", "Jon", "Sloan", "Shane", "Izis"]
    conjoined = "and ".join(students)

    # What will this print?
    print("My students are", conjoined, lineref())

    # Because strings are immutable, join is essential for filtering out elements we don't
    # want from strings. We can do this with the following algorithm:
    #     1) create a list to hold the characters I want to keep
    #     2) loop over the string
    #     3) for every character in the string, determine if it's one you want to keep.
    #        if it is, add it to our list. If it isn't, go to the next item in the loop.
    #     4) when the loop is finished, call the join method on the empty string, passing
    #        the list of saved characters as an argument.
    #
    # let's see this in action.
    badstring = "Punctuation is, like, just extremely ... tedious, you know?"
    goodchars = []

    for char in badstring:
        if char.isalpha() or char.isspace():  # in other words, NOT punctuation
            goodchars.append(char)

    goodstring = "".join(goodchars)

    # What will this print?
    print("The value of goodstring is", goodstring, lineref())

    # 3.                       dict methods
    #
    # There's only one dict method I want to go over here, and that's the 'get' method.
    # the dict 'get' method works a lot like indexing a dict; you give it a key you want the
    # value of, and it gives you back that value. But the 'get' method can also take an optional
    # argument, which is a default value to return if the dict doesn't contain that key.
    # (see documentation at https://docs.python.org/3/library/stdtypes.html#mapping-types-dict for more)

    studentsd = dict(zip(students, ["good student"] * len(students)))

    clinton_student_type = studentsd.get("Clinton", "non-student")

    # What will this print?
    print("Clinton is a", clinton_student_type, "student", lineref())


def comprehensions():
    # Comprehensions are a shorthand way of creating lists and dictionaries. They're based
    # on a blend of for loop syntax and list literal syntax. Below is a simple example using
    # an array of students
    students =  ["Kyle", "Tori", "Robert", "Harrison", "Kim", "Jon", "Sloan", "Shane", "Izis"]

    studentsupper = [s.upper() for s in students]

    # What will this print?
    print("The value of studentsupper is", studentsupper, lineref())

    # a list comprehension is surrounded by square brackets, and contains an expression followed
    # by a for statement that loops through a collection. What makes comprehensions really
    # powerful is the ability to use arbitrary methods, functions, and operators in the
    # expression part of the comprehension.

    # We can also create dict comprehensions, using a very similar syntax. A better way to
    # create the dictionary made on line 710 would be to use a comprehension, as follows:
    sd = {student: "good student" for student in students}

    # The only real difference between this and a list comprehension is the use of curly braces
    # and the need to indicate the key and the value by separating them with a colon (and,
    # obviously, that one is a dict).





if __name__ == "__main__":
    # This section is intended to allow you to run these examples one by one,
    # if you run the file from the command line, or to import the file from a python
    # terminal and play around with these functions and values. I'm also taking it as
    # an opportunity to do something silly by iterating through a list of all the functions
    # in this file and calling them one by one. This is only to show how flexible Python
    # can be about how data is used and what counts as data.
    functions = [index_examples, basic_sequence_functions, for_loop_basics, membership_tests]

    for f in functions:
        f()

        command = input("press 'q' to quit, or any other key to continue.")

        if command == "q":
            break
