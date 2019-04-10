from math import sqrt


def foo1(num):

    try:  # errors are caught in try blocks and handled in except block
        return sqrt(num)

    except ValueError:  # once a ValueError comes up, instead of an error, there can be a custom message do handle the error
        raise ValueError("Cannot square root a negative number")

def fooList(numList):
    """
    Compute the sum of the values in the list
    :param numList:
    :return:
    """
    # check if the list is empty
    try:
        if len(numList) == 0:
            raise ValueError("Cannot process empty list")
        return sum(numList)
    except TypeError:
        raise TypeError("Cannot total non-numbers.")
