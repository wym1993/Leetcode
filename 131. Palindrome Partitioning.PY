class Solution(object):
    def checkPalind(self, word):
        l = 0; r = len(word)-1;
        while(l<r):
            if word[l]!=word[r]:
                return False;
            else:
                l+=1;
                r-=1;
        return True;
    
    def dfs(self, s, temp):
        if len(s)==0: Solution.result.append(temp);
        
        for i in range(1,len(s)+1):
            if self.checkPalind(s[:i])==True:
                self.dfs(s[i:], temp+[s[:i]]);
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.result = [];
        self.dfs(s, []);
        return Solution.result;
    