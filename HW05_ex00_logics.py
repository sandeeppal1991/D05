#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        user_input = int(input("Enter a number to determine if even or odd : "))
        if(user_input % 2 == 0):
            print("It's Even !")
        else:
            print("Its Odd !")
    except Exception as e:
        if(type(e).__name__ == "ValueError"):
            print("You must enter an integer !" )
        else:
            print("Please enter something ! ")
    pass


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    print("#"*100 +"\n\n\nHere is the 10 by 10 grid ! Tada !\n\n\n ")
    iterator = 1
    # using the row_line variable to print a line of numbers
    row_line = ""
    while(iterator <= 100):
        if(iterator % 10 == 0):
            #using the condition to print a new line when the iterator is a multiple of 10
            row_line += "{:<3}".format(str(iterator))
            print(row_line)
            row_line = ""
        else:
            # if the iterator is not a multiple of 10 then keep appending numbers to a row
            row_line += "{:<3}".format(str(iterator))
        iterator += 1


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    print ("\n\nThis program is to find the average of all the numbers you would enter. When you want to see the average of all the numbers that you have enetered, type 'done' ")
    count_of_numbers = 0
    total_value = 0
    try:
        while(True):
            user_input = input("Enter a number : ")
            if(user_input.lower() == "done"):
                print("The Average of the numbers you entered is : " + str(total_value/count_of_numbers))
                break;
            else:
                count_of_numbers += 1
                total_value += int(user_input)
    except Exception as e:
        if(type(e).__name__ == "ValueError"):
            print("You must enter an integer !" )
        else:
            print("Please enter something ! ")
    pass


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """

    pass
    even_odd()
    ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
