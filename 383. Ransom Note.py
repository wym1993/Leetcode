class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomDict = list(magazine);
        for c in ransomNote:
            if not c in ransomDict:
                return False;
            else:
                ransomDict.remove(c);
            
        return True;
        

def canConstruct(self, ransomNote, magazine):
    return not collections.Counter(ransomNote) - collections.Counter(magazine)