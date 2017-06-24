class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = self.formDict(list(set(dictionary)));
    
    def formDict(self, dictionary):
        dic = {};
        for word in dictionary:
            if len(word)<3:
                abb = word;
            else:
                abb = word[0]+str(len(word)-2)+word[-1];
            
            if not abb in dic:
                dic[abb] = [word];
            else:
                dic[abb].append(word);
        
        return dic;

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            check = word;
        else:
            check = word[0]+str(len(word)-2)+word[-1];
        
        # print word, check, not check in self.dic
        if not check in self.dic:
            # self.dic[check] = [word];
            return True;
        else:
            if len(self.dic[check])==1 and self.dic[check][0]==word:
                # print 'False', self.dic[check][0], word
                return True;
            else:
                return False;
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)