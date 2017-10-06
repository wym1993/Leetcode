class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = str(numerator*1.0/denominator);
        if not '.' in result:
            return result;
        else:
            deci_part = result[result.index('.')+1:];
        
        for i in range(len(deci_part)):
            for j in range(i+1,len(deci_part)):
                if self.findSame(deci_part, i, deci_part[i:j]):
                    return 
        
    
    def findSame(self, deci_part, start, part):
        for i in range(start+1, len(deci_part)-len(part)+1):
            if deci_part[i:i+len(part)]==part:
                return True;
        
        return False;