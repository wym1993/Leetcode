class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0 # The complete word
        j = 0
        num = 0
        
        while i < len(word) and j < len(abbr):
           # if  j is letter:
            if ord(abbr[j]) >= ord('a') and ord(abbr[j]) <= ord('z'):
                i = i + num
                if i < len(word) and word[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False
                num = 0
            else: 
                if num == 0 and abbr[j] == '0':
                    return False
                num = num * 10 + int(abbr[j])
                j += 1
                
        return i + num == len(word) and j == len(abbr)