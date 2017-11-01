from collections import defaultdict
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype:List[List[int]]
        """
        store = defaultdict(list)
        for building in buildings:
            store[building[0]].append((1, building[2]));
            store[building[1]].append((-1, building[2]));
            
        curr = [0];
        result = [];
        for timeStamp in sorted(store):
            tmp = max(curr);
            for (act, height) in store[timeStamp]:
                if act==1:
                    curr.append(height);
                else:
                    curr.remove(height);
            if tmp!=max(curr):
                result.append([timeStamp, max(curr)]);
        
        return result;
                
        