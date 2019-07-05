# Discussion Week 3

with open('Dialog.txt', 'r') as inFile:
    fileContents = inFile.read()
    fileWords = fileContents.split()
    for eachWord in fileWords:
        print eachWord
