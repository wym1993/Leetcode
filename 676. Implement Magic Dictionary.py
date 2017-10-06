class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.store.append(word);
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for cand in self.store:
            if len(cand)!=len(word):
                continue;
            else:
                if sum([c1!=c2 for c1, c2 in zip(word, cand)])==1:
                    return True;
        
        return False;
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)