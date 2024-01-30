#!/usr/bin/python3

def add_integer(a, b=98):
    """ function to add to integer

    raise :
    TypeError : if a or b are not integer or floate

    Return: the summtion of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b nust be an integer")
    a = int(a)
    b = int(b)
    return a + b
