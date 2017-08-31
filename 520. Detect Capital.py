class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word==word.lower():
            return True;
        if word == word.upper():
            return True;
        
        if word[0]!=word[0].upper():
            return False;
        else:
            if word[1:]:
                return word[1:]==word[1:].lower();
                