"""
Compare magic numbers with file extensions.

Author: T. Palmer
Initial Release: February 2018  Version 1.0.0

Required System Library: libmagic
Required Python Library: python-magic
"""

import os
import magic
import json
import argparse


class MagicCompare:
    """Responsible for magic number comparison business logic."""

    parsedArgs = None
    extensions = None

    def __init__(self):
        """Magic number comparison constructor."""
        self.setupParsedArguments()
        self.initializeExtensions()

    def perform(self):
        """Perform magic number comparison business logic."""
        path = self.parsedArgs.path
        for filePath in os.listdir(path):
            fullPath = os.path.join(path, filePath)
            fileName, fileExtension = os.path.splitext(fullPath)
            fileExtension = fileExtension.replace('.', '')
            openedFile = self.validateAndOpenFile(fullPath, 'rb')
            if not openedFile:
                continue

            fileContents = self.readFile(openedFile)
            if fileContents and fileExtension:
                print("Checking " + fullPath)
                mime = magic.from_file(fullPath, mime=True)
                if fileExtension in self.extensions:
                    allowedMIME = self.extensions[fileExtension]["mime"]
                    if mime != allowedMIME:
                        print("Discrepancy found:")
                        print("\tMagic detected: " + mime)
                        print("\tLocal found: " + allowedMIME)

    def initializeExtensions(self):
        """
        Initialize the extensions dictionary.
        Source: https://gist.github.com/Qti3e/6341245314bf3513abb080677cd1c93b
        """
        openedJSON = self.openFile('./extensions.json', 'r')
        self.extensions = json.load(openedJSON)

    def setupParsedArguments(self):
        """Initialize parsedArgs."""
        parser = argparse.ArgumentParser(
            'magicCompare'
        )

        parser.add_argument(
            "-p",
            "--path",
            help="Specify the directory to use for comparison",
            required=True
        )

        self.parsedArgs = parser.parse_args()

    def openFile(self, path, mode):
        """Attempt to open the file and return it."""
        try:
            openFile = open(path, mode)
        except IOError:
            self.logger.error('Failed to open: ' + path)
            return
        else:
            return openFile

    def validateAndOpenFile(self, path, mode):
        """If the file is valid, open it and return the opened file."""
        if self.isValidFile(path):
            return self.openFile(path, mode)
        else:
            return False

    def isValidFile(self, path):
        """Verify the path is valid, is not a symbolic link, and is real."""
        if (os.path.exists(path) and
           not os.path.islink(path) and
           os.path.isfile(path)):
            return True
        else:
            return False

    def readFile(self, openedFile):
        """Attempt to read the file contents and return them."""
        try:
            contents = openedFile.read()
        except IOError:
            openedFile.close()
            print('Failed to read: ' + openedFile)
            return
        else:
            return contents


magicCompare = MagicCompare()
magicCompare.perform()
