""" 
Step 1

Make a class named User. Add the following attributes to your class:

    name
    email
    city
    state

Create two different user instances using your class. How can you check their different attributes?


Step 2

Add a __str__ method to your class that displays the identity and attributes of an instance.


Step 3

Make a method named location that returns a string listing the user’s city and state (e.g., “Durham, NC”).


Step 4

Add an attribute called is_active to your class. This attribute should have a default value of True.

Then, make another method called deactivate that changes the value of the is_active attribute to False.

Create an instance of a user and test that it works. Try resetting the attribute to True using the assignment operator and checking the value again.


Step 5

Add an attribute called login_count that keeps a count of how many days in a row a user logs in. Its default value should be 0.

Add a method called increment_login_count that adds 1 to the login_count attribute each time it is called and returns the updated count.

Then add a method called reset_login_count that resets the count to 0.

Create an instance of a user and test that this works.
"""
class User:

    def __init__(self, name, email, city, state, is_active=True, login_count=0):
        self.name = name
        self.email = email
        self.city = city
        self.state = state
        self.is_active = is_active
        self.login_count = login_count

    def __str__(self):
        return f"<User name={self.name} email={self.email} city={self.city} state={self.state} is_active={self.is_active}>"

    def location(self):
        return f"<Location is {self.city}, {self.state}>"

    def deactivate(self):
        self.is_active = False

    def increment_login_count(self):
        self.login_count += 1
        return self.login_count
        
    def reset_login_count(self):
        self.login_count = 0


if __name__ == "__main__":
    # All test cases should go here
    user1 = User("Harrison", "h.arrison@swbell.net", "Durham", "Texas")
    user2 = User("Slaonm", "sloan.bostic@gmail.com", "Raleigh", "North Carolina")

    print("Testing steps 1 & 2")
    print(user1)
    print(user2)
    print()
    print("Testing step 3")
    print(user1.location())
    print(user2.location())
    print()
    print("Testing step 4")
    user1.deactivate()
    user2.deactivate()
    print(user1)
    print(user2)
