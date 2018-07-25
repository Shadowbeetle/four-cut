#!/usr/bin/env python3
"""
Easier credit card number input for non-autofillable online forms.
"""
import sys
import argparse
import pyperclip
from readchar import readchar


def main():
    """main
    main function
    """
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        "-p", "--print", help="print the output and exit", action='store_true')

    args = argument_parser.parse_args()
    input_ = input('Enter the string to be cut: ')
    array_of_fours = [input_[i:i+4] for i in range(0, len(input_), 4)]
    string_of_fours = ' '.join(array_of_fours)

    if args.print:
        sys.exit(0)

    print("%s\n" % string_of_fours)
    print("Printing chunks\n")
    return four_cut(array_of_fours)


def four_cut(array_of_fours, idx=0):
    """four_cut(array_of_fours, idx=0)

    Keyword arguments:
    array_of_fours -- list of stings
    idx -- integer (default 0)
    """
    for (i, chunk) in enumerate(array_of_fours[idx:]):
        print("Next chunk: %s" % chunk)
        print("Would you like to (c)opy or (e)xit [c/e] ", end="", flush=True)
        answer = readchar()

        print(answer)
        if answer == "e":
            sys.exit(0)
        elif answer == "c":
            pyperclip.copy(chunk)
        else:
            print("\nInvalid answer, try again")
            four_cut(array_of_fours, i)


if __name__ == "__main__":
    main()
