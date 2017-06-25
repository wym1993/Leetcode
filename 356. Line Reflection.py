class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        groups = {}
        for x, y in sorted(points):
            if y not in groups:
                groups[y] = [x]
            else:
                groups[y] += x,
       
        poss = None;
        for vals in groups.values():
            minv = min(vals);
            maxv = max(vals);
            mid = (maxv+minv)/2.0
            if not poss:
                poss = mid;
            else:
                if mid!=poss:
                    return False;
                
            for val in sorted(vals):
                if not 2*mid-val in vals:
                    return False;
            
        return True