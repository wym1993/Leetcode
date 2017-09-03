class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        while len(expression)!=1:
            idx = expression.rindex('?');
            if expression[idx-1]=='T':
                expression = expression[:idx-1] + expression[idx+1] + expression[idx+4:];
            else:
                expression = expression[:idx-1] + expression[idx+3:];
        
        return expression
                