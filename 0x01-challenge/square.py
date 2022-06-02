#!/usr/bin/python3
"""Class Square"""


class Square():
    """Object square"""
    __width = 0
    __height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        # width was changed to height
        # (w * w) => (w * h)
        return self.__width * self.__height

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Informal string """
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
