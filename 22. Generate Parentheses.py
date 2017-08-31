class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = [];
        
        def findParent(l, r, temp):
            if l==n and r==n:
                self.result.append(temp);
                return;
                
            if r>l or l>n or r>n:
                return;
            
            temp+='(';
            findParent(l+1, r, temp);
            temp = temp[0:len(temp)-1];
            temp+=')'
            findParent(l,r+1,temp);
            
            return;
        
        findParent(0, 0, "");
        return self.result;