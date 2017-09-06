class TrieNode(object):
    def __init__(self):
        self.childs = dict();
        self.isWord = False;

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode();

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root;
        for letter in word:
            child = node.childs.get(letter);
            if child is None:
                child = TrieNode();
                node.childs[letter] = child;
            node = child;
        node.isWord = True;
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchre(word, self.root);
        
    def searchre(self, word, node):
        for i in range(len(word)):
            if word[i]!='.':
                if node.childs.get(word[i])==None:
                    return False;
                node = node.childs.get(word[i]);
            else:
                for letter in node.childs:
                    child = node.childs[letter];
                    if self.searchre(word[i+1:len(word)], child)==True:
                        return True;
                return False;
        return node.isWord;
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)