from reader import *
import wordTree
from generator import Generator, BackupGenerator, BestMatchGenerator

tree = processFileByWord("C:\Users\Eracoy\Google Drive\MarkovGen\FiftyShadesOfGrey.txt")
tree = processFileByWord("PlanetsInhabited.txt",tree)
#tree = processFileByWord("wikipedia2text-extracted.txt")
tree.printToFile(tree.tree)
seenWords = list("X")
markovGenerator = BestMatchGenerator(tree, seenWords)
outputFile = open("output.txt","w")
for i in range(1000):
    outputFile.write(markovGenerator.nextWord()+" ")
outputFile.close()
#processFile("testInput.txt").printTree()
