class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return len(s)==0;
        
        n = len(s);
        store = [False]*(n+1);
        store[0] = 1;
    
        maxLen = max([len(x) for x in wordDict])
        for i in range(1,n+1):
            for j in range(1, min(i,maxLen)+1):
                if not store[i-j]:
                    continue;
                
                if s[i-j:i] in wordDict:
                    store[i]=True;
                    break;
        
        return store[n];



class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False;
        
        l = max([len(word) for word in wordDict]);
        check = [False for _ in range(len(s)+1)];
        check[0] = True;
        
        for i in range(len(s)):
            if not check[i]:
                continue;
            
            for j in range(i+1, i+l+1):
                if j>len(s):
                    break;
                if s[i:j] in wordDict:
                    check[j]=True;
        return check[-1];
        