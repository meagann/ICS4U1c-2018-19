"""
-------------------------------------------------------------------------------
Name:           practice_address2.py
Purpose:

Author:		    James. M

Created:		21/03/2019
#------------------------------------------------------------------------------
"""


class Address(object):

    def __init__(self):
        self.address_line1 = ""
        self.address_line2 = ""
        self.city = ""
        self.postal_code = ""
        self.province = ""
        self.country = ""

    def print_address(self):
        print(self.address_line1)
        if self.address_line2 != "":
            print(self.address_line2)
        print(self.city + ", " + self.postal_code + ", " + self.province)
        print(self.country)


def main():
    home_address = Address()
    home_address.address_line1 = "123 Main St."
    home_address.address_line2 = "Unit #2"
    home_address.city = "Markham"
    home_address.postal_code = "L3R 8M1"
    home_address.province = "Ontario"
    home_address.country = "Canada"

    home_address.print_address()


main()
