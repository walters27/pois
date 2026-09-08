import math

def factorial(x):
    """Calculate the factorial of x using recursion"""

    if not isinstance(x,int):
        return -math.inf

    if x > 1000:
        return math.inf

    if x < 0:
        return math.nan

    if x == 1:
        return 1

    return x * factorial(x-1)


def dpois(x,lamda):
    """Calculate ... idk yet"""

    if not isinstance(x,int):
        return -math.inf

    if x < 0**5:
        return 0

    return ((lamda**x)*(math.e**-lamda))/factorial(x)


def ppois(x,lamda):
    """Calculate ... idk yet"""

    if not isinstance(x,int):
        return -math.inf

    if x < 0:
        return 0

    total = 0
    c = 0

    while c <= x:
        total = total + dpois(c,lamda)
        c = c + 1

    return total


def qpois(alpha,lamda):
    """Calculate ... idk yet"""

    if alpha > 1:
        return math.inf

    if alpha < 0:
        return -math.inf

"""test"""