def avg(a, b):
    """ This simple helper gets the average of two numbers.
        It will be used when adding two Colors.
    """
    return (a + b) // 2  # // will divide and round all in one.


def favg(a, b):
    """ This simple helper gets the average of two numbers.
        It will be used when adding two Colors. Unlike avg,
        it does not round the result.
    """
    return (a + b) / 2


def normalize_rgb(color_value: int) -> int:
    if color_value < 0:
        return 0

    elif color_value > 255:
        return 255

    else:
        return color_value
    

def normalize_alpha(alpha_value: float) -> float:
    if alpha_value < 0.0:
        return 0.0

    elif alpha_value > 1.0:
        return 1.0

    else:
        return alpha_value


class Color:
    """ This class represents a color in RGBA format. Because colors can be mixed to
        produce a new color, this class implements __add__. The __init__ method will ensure
        that r, g, and b are between 0 and 255, and a is between 0 and 1.
    """
    def __init__(self, r, g, b, a=1.0):
        # Make sure r, g, and b are between 0 and 255 and
        # make sure alpha is between 0.0 and 1.0
        self.r = normalize_rgb(r)
        self.g = normalize_rgb(g)
        self.b = normalize_rgb(b)
        self.a = normalize_alpha(a)

    def liked_by_bob_ross(self):
        return True

    def __add__(self, other):
        if not isinstance(other, Color):
            raise TypeError("Cannot add Color and non-Color.")

        else:
            r = avg(self.r, other.r)
            g = avg(self.g, other.g)
            b = avg(self.b, other.b)
            a = favg(self.a, other.a)

            return Color(r,g,b,a)

    def __repr__(self):
        # Delegate to __str__
        return self.__str__()

    def __str__(self):
        return f"<Color r={self.r} g={self.g} b={self.b} a={self.a}>"
