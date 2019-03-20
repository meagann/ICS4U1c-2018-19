class Rectangle(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


def main():

    rectangle1 = Rectangle(5,7)
    rectangle2 = Rectangle(2,8)
    rectangle3 = Rectangle(10,4)
    print("The area of the 3 rectangles are", rectangle1.get_area(), (rectangle2.get_area()), rectangle3.get_area())


main()
