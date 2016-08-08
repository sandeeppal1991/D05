#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def print_words():
    file_object = open("words.txt")
    for word in file_object:
        if(len(word.strip()) > 20 ):
            print(word)

##############################################################################
def main():
    pass  # Call your functions here.
    print("\n\nThe words which are more than 20 characters in the file words.txt are : \n\n")
    print_words()

if __name__ == '__main__':
    main()
