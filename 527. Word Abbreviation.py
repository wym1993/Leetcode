from collections import defaultdict
class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        self.store = {};
        self.solver(dict, 1);
        return map(self.store.get, dict)
    
    def abbr(self, word, size):
        if len(word)<=3 or len(word[size:])==2:
            return word;
        
        return word[:size]+str(len(word[size:])-1)+word[-1];
    
    def solver(self, dict, size):
        tmp = defaultdict(list);
        for word in dict:
            tmp[self.abbr(word, size)].append(word);
        
        for abbr, wList in tmp.iteritems():
            if len(wList)==1:
                self.store[wList[0]]=abbr;
            else:
                self.solver(wList, size+1);