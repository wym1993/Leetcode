class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [];
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c);
            else:
                if not stack:
                    return False;
                r = stack.pop();
                if c==')' and r!='(':
                    return False;
                if c==']' and r!='[':
                    return False;
                if c=='}' and r!='{':
                    return False;
        
        return not stack;