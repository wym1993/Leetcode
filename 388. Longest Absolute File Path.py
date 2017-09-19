class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0;
        rest = input.split('\n');
        rest.reverse();
        tmp = [];
        lmax = 0
        while rest:
            dir = rest.pop();
            num = dir.count('\t');
            tmp = tmp[:num]+[dir[num:]];
            if '.' in dir[num:]:
                lmax = max(len('/'.join(tmp)), lmax);
        
        return lmax;
        