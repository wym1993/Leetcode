class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        result = (C-A)*(D-B)+(G-E)*(H-F)
        l1, r1 = max(A, E), max(B, F);
        l2, r2 = min(C, G), min(D, H);
        
        if l1>=l2 or r1>=r2:
            return result;
        else:
            return result-(l2-l1)*(r2-r1);