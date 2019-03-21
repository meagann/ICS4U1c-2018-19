"""
-------------------------------------------------------------------------------
Name:           practice_point.py
Purpose:

Author:		    James. M

Created:		21/03/2019
------------------------------------------------------------------------------
"""
import math


class Point(object):

    def __init__(self, x, y):
        """
        Create an instance of a Point
        :param x: x coordinate value
        :param y: y coordinate value
        """
        self.x = x
        self.y = y

    def get_distance(self, other_point):
        """
        Compute the distance between the current object and another point
        :param other_point: Point object to find the distance to
        :return: float
        """
        distance_x = other_point.x - self.x
        distance_y = other_point.y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        # distance = math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
        # distance = (distance_x**2 + distance_y**2)**0.5
        return distance


def main():
    """
    Program demonstrating the creation of point instances and calling class methods
    """
    point1 = Point(3, 4)
    point2 = Point(4, 7)

    print("The distance between the points is", round(point1.get_distance(point2), 2))


main()
