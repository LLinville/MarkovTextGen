from wordTree import WordTree
import pickle
import string

def processFileByWord(filename, inputTree = None):
    file = open(filename)
    fileLinesLength = sum([1 for line in file])
    file.close()
    file = open(filename)
    lineno = 1

    if inputTree is not None:
        tree = inputTree
    else:
        tree = WordTree(None, None)
    seenWords = list("a"*3)

    for line in file:
        if lineno % 100 == 0:
            print "Processing line " + str(lineno) + " / " + str(fileLinesLength)
        for seenWord in line.replace("\n"," ").lower().split(" "):
            seenWord.replace(" ","")
            if seenWord == "":
                continue
            tree.addPath(seenWords)
            seenWords = seenWords[1:]
            seenWords.append(seenWord)

        lineno += 1

    return tree

def processFileByAlphanum(filename, inputTree = None):
    file = open(filename)
    fileLinesLength = sum([1 for line in file])
    file.close()
    file = open(filename)
    lineno = 1

    if inputTree is not None:
        tree = inputTree
    else:
        tree = WordTree(None, None)

    seenWords = list("a"*10)

    for line in file:
        if lineno % 100 == 0:
            print "Processing line " + str(lineno) + " / " + str(fileLinesLength)
        for seenWord in list(line):

            tree.addPath(seenWords)
            seenWords = seenWords[1:]
            seenWords.append(seenWord)
        line = filter(lambda x: x in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ", line)

        lineno += 1

    return tree