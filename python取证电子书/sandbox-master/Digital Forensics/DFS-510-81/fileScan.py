"""
Calculate MD5 Hash of files in provided directory.

Author: T. Palmer
Initial Release: February 2018  Version 1.0.0

Required PyPI Library: texttable
"""

import os
import argparse
import hashlib
import time
import logging
from texttable import Texttable

# 5) If you encounter an exception while processing the files write the
#    information associated with the exception to a python log file
logging.basicConfig(
    filename='fileScanLog.log',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s'
)
logger = logging.getLogger('com.palmer.filescan')


class FileScan:
    sortedFileList = []
    parsedArgs = None

    def perform(self):
        # 1) Allow a user to specify a directory
        parser = argparse.ArgumentParser(
            'Calculate MD5 Hash of files in provided directory'
        )

        parser.add_argument(
            "-d",
            "--path",
            help="Specify the directory to hash",
            required=True
        )

        self.parsedArgs = parser.parse_args()
        path = self.parsedArgs.path

        # 2) Validate that the directory exists
        if not os.path.exists(path):
            logger.error("Please provide a valid directory")
            return

        # 3) Using the OS module and the function os.listdir() obtain the list
        #    of files that exist in the specified directory.
        tempDictionary = {}
        for filePath in os.listdir(path):
            fullPath = os.path.join(path, filePath)
            openedFile = self.validateAndOpenFile(fullPath, 'rb')
            if not openedFile:
                break

            fileContents = self.readFile(openedFile)
            if fileContents:
                hashValue = self.fileHash(fileContents)
                localModifiedTime = time.ctime(os.path.getmtime(fullPath))

                # Store relevant data points in a dictionary using the path
                # as the key
                tempDictionary[fullPath] = {
                    'name': os.path.basename(fullPath),
                    'sizeInBytes': os.path.getsize(fullPath),
                    'modifiedTime': localModifiedTime,
                    'md5': hashValue
                }

            openedFile.close()

        # Sort the dictionary by file size
        self.sortedFileList = sorted(
            tempDictionary.items(),
            key=lambda x: x[1]['sizeInBytes'],
            reverse=True
        )
        self.generateReport()

    def generateReport(self):
        # 4) For each file in the directory produce the following output for
        # each File; sorted by FileSize (largest file first)
        #
        #    Path    FileName    FileSize   Last-Modified-Time  MD5 Hash
        #
        # Use the texttable module to format the output in a more
        # human-readable format
        table = Texttable()
        table.add_row([
            "Path",
            "FileName",
            "FileSize",
            "Last-Modified-Time",
            "MD5-Hash"
        ])
        for path, fileDictionary in self.sortedFileList:
            table.add_row([
                path,
                fileDictionary["name"],
                fileDictionary["sizeInBytes"],
                fileDictionary["modifiedTime"],
                fileDictionary["md5"]
            ])
        print(table.draw())

    # If this file is valid, attempt to open it and return the opened file
    def validateAndOpenFile(self, path, mode):
        if self.isValidFile(path):
            return self.openFile(path, mode)
        else:
            return None

    # Verify that the path is valid, is not a symbolic link, and is real
    def isValidFile(self, path):
        if (os.path.exists(path) and
           not os.path.islink(path) and
           os.path.isfile(path)):
            return True
        else:
            logger.error(path + ' is not a valid file.')
            return False

    # Attempt to open the file and return it
    def openFile(self, path, mode):
        try:
            openFile = open(path, mode)
        except IOError:
            logger.error('Failed to open: ' + path)
            return
        else:
            return openFile

    # Attempt to read the file contents and return them
    def readFile(self, openedFile):
        try:
            contents = openedFile.read()
        except IOError:
            openedFile.close()
            logger.error('Failed to read: ' + openedFile)
            return
        else:
            return contents

    # Calcuate an MD5 hash of given contents
    def fileHash(self, contents):
        hash = hashlib.md5()
        hash.update(contents)
        hexMD5 = hash.hexdigest()
        return hexMD5.upper()


scanner = FileScan()
scanner.perform()
