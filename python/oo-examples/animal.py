""" Python OO examples.
"""

# This is the simplest kind of class - it stores named data attributes and provides a basic
# interface to Python with the __str__ method (provides a printable string representation)
# and the __repr__ method (provides a more detailed string representation for debugging/working 
# in the command line).
class Animal:
    """ Represents a member of the kingdom animalia.
    """
    def __init__(self, name, age, species):
        """ Initialize instance attributes.
        """
        self.name = name
        self.age = age
        self.species = species.lower()  # ignore case by calling lower on self.species 

    def birthday(self):
        # Age this animal by one year
        print("Happy birthday!")
        self.age = self.age + 1

    def __repr__(self):
        return f"<Animal name='{self.name}' age={self.age} species='{self.species}'>"

    def __str__(self):
        return f"Hello, my name is {self.name}."


# A fundamental concept in Object Oriented Programming is 'inheritance', the creation of a new class from an
# existing class. When one class inherits from another, it receives all the attributes and behavior of the
# 'parent' class. However, it can be customized by OVERRIDING the parent class (implementing methods
# with the same name that do something different) or EXTENDING the parent (adding new methods or attributes.)
# The Person class below inherits from Animal. It overrides Animal's __init__ and __repr__ methods and adds
# a new method, is_walkin_here, which returns true if the instance of Person is walkin' here.
class Person(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.species = "human"

    def is_walkin_here(self):
        if self.name == "Dustin Hoffman":
            return True

        else:
            return False

    def __repr__(self):
        return f"<Person name={self.name} age={self.age} species={self.species}>"


# Here's a slightly more complicated class that uses a list to store
# information about a population of animals. Each Animal is represented as
# an animal class object. Because this is a collection, we'll implement
# some of Python's builtin methods for collections.
class Population:
    """ Represnts a population of animals of the same species.
    """
    def __init__(self, species, members):
        self.members = []
        self.species = species.lower()  # ignore case by calling lower on self.species

        for member in members:
            self.add(member)

    def add(self, animal):
        # Raise a value error if the supplied animal is not the same species
        # as self.species
        if animal.species != self.species:
            raise ValueError(f"Incompatible species {animal.species}.")

        self.members.append(animal)

    def __iter__(self):
        # just delegate to self.members by passing it to iter builtin function
        return iter(self.members)

    def __contains__(self, animal):
        # Just delegate to self.members
        return animal in self.members

    def __str__(self):
        return f"Population(species={self.species}, members={self.members})"


if __name__ == "__main__":
    # make a list of kitty names
    kitty_names = ["Charli", "Buddy", "Kitty", "Mr. Haystacks", "Saga", "Sebastian", "Petunia", "BabyGirl", "Philbert"]
    # make a list of kitty Animal objects
    kitties = []

    for name in kitty_names:
        kitty = Animal(name, 1, "cat")
        kitties.append(kitty)
    
    # Create a population from the list of kitty Animal objects
    our_kitties = Population("cat", kitties)

    for kitty in our_kitties:
        print(f"{kitty.name} is a kitty!")

    hobbes = Animal("Hobbes", 11, "cat")

    if hobbes in our_kitties:
        print("Hobbes is already playing with the other kitties.")

    else:
        print("Hobbes is lonely :(")
        our_kitties.add(hobbes)
