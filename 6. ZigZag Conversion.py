class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:
            return s;
        temp = [];
        for i in range(numRows):
            temp.append("");
        
        index = -1;
        step = 1;
        for i in range(len(s)):
            index+=step;
            if index==numRows:
                index-=2; step = -1;
            if index==-1:
                index=1; step = 1;
            temp[index]+=s[i];
        
        return ''.join(temp);