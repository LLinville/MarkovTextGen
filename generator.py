class Generator:
    def __init__(self, tree, seenWords):
        self.tree = tree
        self.seenWords = seenWords

    def nextWord(self):
        nextWordTree, depth = self.tree.search(self.seenWords)
        print depth
        chosenChild = nextWordTree.randomChild()
        self.seenWords = self.seenWords[1:]
        self.seenWords.append(chosenChild.word)
        return chosenChild.word

class BackupGenerator:
    def __init__(self, tree, seenWords):
        self.tree = tree
        self.output = seenWords
        self.minimumDepth = 2
        self.seenWordsSize = 7

    def nextWord(self):
        nextWordTree, depth = self.tree.search(self.output[-1*self.seenWordsSize:])
        print depth
        # while depth < self.minimumDepth and len(self.output):
        #     print "Backing up at length "+str(len(self.output))
        #     print self.output
        #     self.output = self.output[:-1]
        #     nextWordTree, depth = self.tree.search(self.output[-1*self.seenWordsSize:])
        chosenChild = nextWordTree.randomChild()
        self.output.append(chosenChild.word)
        return chosenChild.word

class BestMatchGenerator:
    def __init__(self, tree, seenWords):
        self.tree = tree
        self.output = seenWords
        self.maxSearchWidth = 8

    def nextWord(self):
        for searchWidth in range(1,self.maxSearchWidth+1)[::-1]:
            nextWordTree, depth = self.tree.search(self.output[-1*searchWidth:])
            if depth == searchWidth:
                break
        print depth
        # while depth < self.minimumDepth and len(self.output):
        #     print "Backing up at length "+str(len(self.output))
        #     print self.output
        #     self.output = self.output[:-1]
        #     nextWordTree, depth = self.tree.search(self.output[-1*self.seenWordsSize:])
        chosenChild = nextWordTree.randomChild()
        self.output.append(chosenChild.word)
        return chosenChild.word