#  A demonstration of the input command


print("Welcome!")

students = ["Sloan", "Shane", "Tori", "Izis", "Robert", "Kyle", "Kim", "Harrison"]


while True:
    msg = input("What's on your mind? ")
    msg = msg.lower()
    print()

    if msg == 'quit':
        print("Yeah, I'm pretty busy too, I'll catch you later.")
        break

    elif msg == "loop-demo":
        print("Demonstrating loop through values: ")

        for student in students:
            print(f"{student} is a great student!")

        print()
        print("Demonstrating filtering student name by first letter (comprehension): ")

        kstudents = [s for s in students if s[0].lower() == "k"]

        # the code on 27 is equivalent to

        # kstudents = []
        # for s in students:
        #     if s[0].lower() == "k":
        #         kstudents.append(s)

        kstudents_upcase = [s.upper() for s in students if s[0].lower() == "k"]

        print("Upcased students with 'k's: ")
        for ks in kstudents_upcase:
            print(ks)
        
    else:
        print(f"Wow, really, {msg}? That's so interesting.")
        print()
 
