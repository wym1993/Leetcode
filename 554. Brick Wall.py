class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not wall or not wall[0]:
            return 0;
        
        store = {};
        for row in wall:
            i = 0;
            for num in row[:-1]:
                i+=num
                store[i] = store.get(i, 0)+1;
        return len(wall)-max(store.values()+[0]);