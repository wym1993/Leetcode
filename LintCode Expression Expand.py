class Solution:
    """
    @param: s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = [];
        number = 0;
        for c in s:
            if c.isdigit():
                number = number*10 + int(c);
            elif c=='[':
                stack.append(number);
                number = 0;
            elif c==']':
                strs = [];
                while len(stack):
                    k = stack.pop();
                    if type(k) == int:
                        stack.append(''.join(reversed(strs))*k);
                        break;
                    strs.append(k);
            else:
                stack.append(c);
        
        return ''.join(stack);