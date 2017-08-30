class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        test = list(s)
        cand = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
        if not s:
            return s;
        left, right = 0, len(s)-1;
        
        while left<right:
            while left<right and test[left] not in cand:
                left+=1;
            
            while right>left and test[right] not in cand:
                right-=1;
            
            test[left], test[right]= test[right], test[left];
            left+=1;
            right-=1;
            
        return ''.join(test);