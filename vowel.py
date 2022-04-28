#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that checks if a letter is a vowel


def main():
    # This is the main program

    # Input

    letter = input("Enter a Letter: ")

    # Process and Output

    if (
        letter == "a"
        or letter == "e"
        or letter == "i"
        or letter == "o"
        or letter == "u"
    ):
        print("\nYour Letter is a Vowel!")
    elif letter == "y":
        print("\nThat's Sometimes a Vowel!")
    else:
        print("\nThat's Not a Vowel")
    print("\nDone.")


if __name__ == "__main__":
    main()
