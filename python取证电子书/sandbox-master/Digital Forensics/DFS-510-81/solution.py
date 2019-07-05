"""
Extract the magic number of a file.

Author: T. Palmer
Initial Release: February 2018  Version 1.0.0
"""

import os
import argparse
import hashlib
import logging
import time
import binascii
from itertools import izip_longest


class MagicFinder:
    """Responsible for magic number extraction business logic."""

    parsedArgs = None
    logger = None
    outputFile = None
    inputFileStats = None

    def __init__(self):
        """Magic number finder constructor."""
        self.setupParsedArguments()

        # A welcome message will be displayed along with the details of the
        # arguments specified by the user.  If the verbose option is NOT
        # specified, you will run silently unless a major error occurs.
        self.printOut("DFS-510 Week 7 Solution")
        self.printOut("Professor Hosmer, February 2018\n")
        self.printOut("Input File: " + self.parsedArgs.inputFile.name)
        self.printOut("Output File: " + self.parsedArgs.outputFile)
        self.printOut("Log File: " + self.parsedArgs.logFile + "\n")
        self.printOut("Creating Log File")
        self.setupLogger()
        self.logger.info("Week 7 Solution, Professor Hosmer")

    def perform(self):
        """Perform magic number extraction business logic."""
        self.printOut("Extracting File Stats ...")
        self.inputFileStats = os.fstat(self.parsedArgs.inputFile.fileno())
        localModifiedTime = time.ctime(self.inputFileStats.st_mtime)

        self.printOut("Reading the Input File Contents ...")
        inputContents = self.readFile(self.parsedArgs.inputFile)
        self.logger.info(
            "File: " + self.parsedArgs.inputFile.name +
            " Read the file stats Success"
        )

        self.printOut("Hashing the File Contents - SHA256 ...")
        fileHash = self.fileHash(inputContents)
        self.logger.info(
            "File: " + self.parsedArgs.inputFile.name +
            " SHA256: " + fileHash
        )
        self.printOut("Reading the first 32 bytes of the file ...")
        magicNumber = self.magicNumber(inputContents)
        self.logger.info(
            "File: " + self.parsedArgs.inputFile.name +
            " Header Read: " + magicNumber
        )

        self.printOut("Creating the Output File and Recording the Results ...")
        # 3) Validate the outputFile during creation. if any errors occur
        #    report and log them and abort the script.
        # 5c) Open the output file for writing
        # Record information about the input file: File Path, File Size,
        # Last-Modified-Time
        self.outputFile = self.openFile(self.parsedArgs.outputFile, 'w')
        self.outputFile.write(
            "File Name: " + self.parsedArgs.inputFile.name + "\n"
        )
        self.outputFile.write(
            "File Size: " + str(self.inputFileStats.st_size) + "\n"
        )
        self.outputFile.write("File Modified: " + localModifiedTime + "\n")
        self.outputFile.write("SHA256 Hash: " + fileHash + "\n")
        self.outputFile.write("File Header: " + magicNumber + "\n")

        # 5f) Record information about the output file to the log (and to the
        #     screen if verbose is selected)
        # 5e) Close Both Files once all bytes have been written
        self.parsedArgs.inputFile.close()
        self.outputFile.close()
        self.printOut("Script Complete")

    def setupParsedArguments(self):
        """Initialize parsedArgs."""
        parser = argparse.ArgumentParser(
            'solution'
        )

        # -v verbose (optional)
        parser.add_argument(
            "-v",
            "--verbose",
            help="Be more verbose with output",
            action="store_true"
        )

        # 1) Validate the inputFile exists, and is readable within argparse.
        #    Report any errors and abort.
        # -i inputFile (this argument is mandatory and requires the user to
        #    specify a single input file)
        # 5b) Open the input file for "read-binary"
        parser.add_argument(
            "-i",
            "--inputFile",
            help="The file to extract the magic number from",
            type=argparse.FileType('rb'),
            required=True
        )

        # -o outputFile (this argument is mandatory and requires the user to
        #    specify a single output file)
        parser.add_argument(
            "-o",
            "--outputFile",
            help="The file to write magic number information to",
            required=True
        )

        # -l logFile (this argument will specify the log file to be used to
        #    record results and exceptions)
        parser.add_argument(
            "-l",
            "--logFile",
            help="The file to log activity information to",
            default='magicFinderLog.log'
        )

        self.parsedArgs = parser.parse_args()

    def setupLogger(self):
        """Initialize logger."""
        # 2) Validate the logFile during creation.  If any errors occur report
        #    them and abort.
        # 5a) Setup the logfile for recording information
        logging.basicConfig(
            filename=self.parsedArgs.logFile,
            level=logging.DEBUG,
            format='%(asctime)s %(message)s'
        )
        self.logger = logging.getLogger('com.palmer.magicfinder')

    def printOut(self, message):
        """If the verbose option is set, print the passed message."""
        # 4) If the verbose option is specified then meaningful output is
        #    provided for each major step of the script.
        if self.parsedArgs.verbose:
            print(message)

    def openFile(self, path, mode):
        """Attempt to open the file and return it."""
        try:
            openFile = open(path, mode)
        except IOError:
            self.logger.error('Failed to open: ' + path)
            return
        else:
            return openFile

    def readFile(self, openedFile):
        """Attempt to read the file contents and return them."""
        try:
            contents = openedFile.read()
        except IOError:
            openedFile.close()
            self.logger.error('Failed to read: ' + openedFile)
            return
        else:
            return contents

    def fileHash(self, contents):
        """Calcuate the SHA256 hash of the passed file contents."""
        hash = hashlib.sha256()
        hash.update(contents)
        hexSHA256 = hash.hexdigest()
        return hexSHA256.upper()

    def magicNumber(self, contents):
        """Parse the magic number from the passed file contents."""
        # 5d) Read the first 32 bytes of the inputFile and convert them to a
        # Hex ASCII representation using the binascii standard library.
        asciiContents = binascii.hexlify(contents[:32])
        tuples = self.grouper(asciiContents, 2)

        # Map the returned array of tuples, and join on '-'
        formattedOutput = '-'.join(map(lambda x: ''.join(x), tuples))
        return formattedOutput

    def grouper(self, iterable, n, fillvalue=None):
        """
        Slice a string into groups.

        Source:
            https://docs.python.org/3/library/itertools.html#itertools-recipes
        """
        args = [iter(iterable)] * n
        return list(izip_longest(*args, fillvalue=fillvalue))


magicFinder = MagicFinder()
magicFinder.perform()
