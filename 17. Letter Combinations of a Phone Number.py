class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return[];
            
        self.letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs" , "tuv", "wxyz"];
        self. result = []
        
        def findComb(digits, index, temp):
            if index==int(len(digits)):
                self.result.append(temp);
                return;
            
            for i in self.letters[int(digits[index])]:
                temp = temp + i
                findComb(digits, index+1, temp);
                temp  = temp[0:len(temp)-1];
        
            return
    
        findComb(digits, 0, "");
        return self.result;