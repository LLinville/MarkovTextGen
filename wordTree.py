import random
class WordTree:
    def __init__(self, word, parent):
        self.word = word
        self.timesSeen = 0
        self.children = []
        self.parent = parent

    def addPath(self, pathWords):
        self.timesSeen += 1
        if not pathWords:
            return
        currentWord = pathWords[0]
        for child in self.children:
            if child.word == currentWord:
                child.addPath(pathWords[1:])
                return
        else:
            child = WordTree(currentWord, self)
            child.addPath(pathWords[1:])
            self.children.append(child)

    def search(self,searchWords, depth=0):
        if not searchWords:
            return self, depth
        for child in self.children:
            if child.word == searchWords[0]:
                # if self.timesSeen > 1:
                return child.search(searchWords[1:], depth=depth+1)
                # else:
                #     return self, depth
        return self, depth

    def randomChild(self):
        pickBound = random.uniform(0,self.timesSeen)
        current = 0
        for child in self.children:
            current += child.timesSeen
            if current >= pickBound:
                # if child.word is None:
                #     print "returning self"
                #     return self
                return child

    def printTree(self, depth = 0):
        print "\t"*depth, self.word, self.timesSeen
        for child in self.children:
            child.printTree(depth = depth+1)

    def toDict(self):
        dict = {}
        for child in self.children:
            dict["W"+child.word] = child.toDict()
            dict["C"] = self.timesSeen
        return dict

    def printToFile(self, file, depth = 0):
        file.write(str(depth) + " " + str(self.word) + " " + str(self.timesSeen) + "\n")
        for child in self.children:
            child.printToFile(file, depth = depth+1)

    @staticmethod
    def readFromFileIterative(file):
        pDepth, pWord, pCount = file.readLine.split(" ")
        lineno = 0
        for line in file:
            lineno += 1
            print "Reading line " + str(lineno)
            for depth, word, count in line.split(" "):
                depth

            pDepth, pWord, pCount = depth, word, count

    @staticmethod
    def constructNodeFromNextLine(file):
        depth, word, count = file.readLine().split(" ")



tree = WordTree(None, None)
tree.addPath("a b c".split(" "))
tree.addPath("a b b".split(" "))
tree.addPath("a c a".split(" "))
tree.addPath("b c c".split(" "))
tree.printTree()
file = open("tree.tree", "w")
tree.printToFile(file)
file.close()
print tree.toDict()
#
# searched = tree.search("a b b".split(" "))
# print [searched.randomChild().word for i in range(10)]