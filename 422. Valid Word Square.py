class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if not words:
            return True;
        
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j>=len(words) or i>=len(words[j]) or words[i][j]!=words[j][i]:
                    return False;
                
        return True;
                