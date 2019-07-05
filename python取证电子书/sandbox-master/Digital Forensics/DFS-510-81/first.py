#!/usr/bin/python
#
# first : Search a hard-coded string
# Author: T. Palmer
#
# Initial Release: January 2018  Version 1.0.0


def main():
    testString = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

    # Capture command-line user input using raw_input
    searchWord = raw_input("Please enter search term: ")

    # If the word is found, save the index to foundIndex
    foundIndex = testString.find(searchWord)

    # If no word was found, find() returns an index of -1
    termFound = "found" if foundIndex != -1 else "not found"

    print searchWord, "was", termFound


main()
