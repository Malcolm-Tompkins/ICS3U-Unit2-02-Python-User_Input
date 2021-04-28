#!/usr/bin/env/ python3

# Created by Malcolm Tompkins
# Created on April 27, 2021
# Calculates the perimeter and area of user input


def main():
    # function that calculates area and perimeter of quadrilateral

    Length = int(input("Input length of quadrilateral: "))
    Width = int(input("Input width of quadrilateral: "))
    # user input

    Area = Length * Width
    Perimeter = (Length + Width) * 2
    # process

    print("\nArea is = {}".format(Area))
    print("Perimeter is = {}".format(Perimeter))
    # output


if __name__ == "__main__":
    main()
