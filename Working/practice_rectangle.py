class Rectangle(object):

    def __init__(self):
        self.width = 0
        self.height = 0


def get_area(rec):

    area = rec.width * rec.height
    return area


def main():

    rect1 = Rectangle()

    rect1.width = int(input("Enter width: "))
    rect1.height = int(input("Enter height: "))

    print("The area of that rectangle is", get_area(rect1))


main()
