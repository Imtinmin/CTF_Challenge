"""
Extract information from a given logfile.

Author: T. Palmer
Initial Release: February 2018  Version 1.0.0
"""

import os
import argparse


class LogScan:
    foundWorms = {}
    parsedArgs = None

    def perform(self):
        # 1) Prompt the user for the log file name (via command line)
        parser = argparse.ArgumentParser(
            'Generate a report from a given log file'
        )
        parser.add_argument(
            "-f",
            "--fileName",
            help="Specify the log file to examine",
            required=True
        )
        parser.add_argument(
            '-o',
            '--output',
            help='Specify the report filename',
            default='logScanReport.txt'
        )

        self.parsedArgs = parser.parse_args()
        fileName = self.parsedArgs.fileName

        if not os.path.exists(fileName):
            print "Please provide a valid filename"
            return

        # 2) Attempt to open the file, and provide a meaningful error message
        #    if anything goes wrong
        fileContents = self.validateAndOpenFile(fileName, 'r')
        if fileContents:
            # 3) For each line in the file
            #    a) Determine if the line contains the word "worm"
            #    b) Create a list of worms that are identified throughout the
            #       file
            for lineNumber, line in enumerate(fileContents):
                # Create a list of all the words on this line and iterate
                # across it
                lineList = line.split(' ')
                for element in lineList:
                    if "worm" in element.lower():
                        count = 1
                        numbers = [lineNumber]
                        # If the worm has already been found, increase the
                        # count and add the line number to the list
                        if element in self.foundWorms:
                            existing = self.foundWorms[element]
                            count = existing["count"] + 1
                            numbers = existing["lineNumbers"] + [lineNumber]
                        # Store the relevant data points in a dictionary
                        # using the worm name as the key
                        self.foundWorms[element] = {
                            "lineNumbers": numbers,
                            "count": count
                        }

    # 4) Generate a report that contains the information regarding each
    #    UNIQUE worms identified
    def generateReport(self):
        if len(self.foundWorms.keys()) > 0:
            output = self.openFile(self.parsedArgs.output, 'w')
            for foundWorm in self.foundWorms:
                lineNumbers = str(self.foundWorms[foundWorm]["lineNumbers"])
                lineNumbers = "".join([str(x) for x in lineNumbers])
                count = str(self.foundWorms[foundWorm]["count"])
                times = "times"
                if count == "1":
                    times = "time"
                print("Found " + foundWorm)
                output.write(
                    "Found " + foundWorm + " " + count + " " + times +
                    " on lines " + lineNumbers + "\n"
                )
            output.close()
            print("Report saved to " + self.parsedArgs.output)
        else:
            print("No instances of 'worm' found.")

    # If this file is valid, attempt to open it and return the opened file
    def validateAndOpenFile(self, path, mode):
        if self.isValidFile(path):
            return self.openFile(path, mode)

    # Verify that the path is valid, is not a symbolic link, and is real
    def isValidFile(self, path):
        if (os.path.exists(path) and
           not os.path.islink(path) and
           os.path.isfile(path)):
            return True
        else:
            print(path + ' is not a valid file.')

    # Attempt to open the file and return it
    def openFile(self, path, mode):
        try:
            openFile = open(path, mode)
        except IOError:
            print('Failed to open: ' + path)
            return
        else:
            return openFile


scanner = LogScan()
scanner.perform()
scanner.generateReport()
