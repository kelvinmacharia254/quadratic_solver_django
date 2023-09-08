import math

class Quadratic:
    """
    This is a quadratic class.
    """

    def __init__(self, **kwargs):
        self.a = kwargs["a"]
        self.b = kwargs["b"]
        self.c = kwargs["c"]

    def is_quadratic(self):
        """
        Checks whether the quadratic equation is valid by checking coefficient a
        :return: True or False
        """
        if self.a == 0:  # if a = 0 then the quadratic equation is not valid. Therefore, return False.
            return False
        else:  # if a is not 0 then the quadratic equation is valid. Therefore, return True.
            return True

    def equation(self):
        """
        Form the quadratic equation
        :return: quadratic equation as a string
        """
        return "No equation generated for now."

    def discriminant(self):
        """
        Computes the discriminant which informs about the nature of the roots.
        :return: discriminant
        """
        discriminant = round(((self.b ** 2) - (4 * self.a * self.c)), 2)
        return discriminant

    def roots(self):
        """
        Compute the roots.
        :return: roots of the quadratic equation as a tuple object with two items.
        """
        discriminant = self.discriminant()
        if discriminant == 0:
            # if discriminant is equal to zero, there is only one root:
            root = round(((-self.b / (2 * self.a)) + ((math.sqrt(discriminant)) / (2 * self.a))), 4)
            return root
        elif discriminant > 0:
            # if discriminant is greater than zero, there are two real roots:
            root1 = round((((-self.b) / (2 * self.a)) + ((math.sqrt(discriminant)) / (2 * self.a))), 4)
            root2 = round((((-self.b) / (2 * self.a)) - ((math.sqrt(discriminant)) / (2 * self.a))), 4)
            return root1, root2
        else:
            # if the discriminant is less than zero then roots are not real i.e. a complex solution is obtained.
            root1 = complex((round(((-self.b) / (2 * self.a)), 4)),
                            (round((-(math.sqrt(abs(discriminant))) / (2 * self.a)), 4)))
            root2 = complex((round(((-self.b) / (2 * self.a)), 4)),
                            (round(((math.sqrt(abs(discriminant))) / (2 * self.a)), 4)))
            return root1, root2


if __name__ == "__main__":
    q = Quadratic(a=1, b=2, c=1)
    print(q.roots())