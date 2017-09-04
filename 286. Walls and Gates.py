class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype:void Do not return anything, modify rooms in-place instead.
        """
        def neighbors(i, j, step, rooms):
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<=x<len(rooms) and 0<=y<len(rooms[0]) and step<rooms[x][y]:
                    yield((x, y), step);
        queue = set([((i, j), 0) for i in range(len(rooms)) for j in range(len(rooms[0])) if rooms[i][j]==0]);
        while queue:
            next_q = set();
            for (i, j), step in queue:
                rooms[i][j]=step;
            for (i, j), step in queue:
                next_q.update(neighbors(i, j, step+1, rooms));
            queue = next_q;
            

    def wallsAndGates(self, rooms):
        q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
        for i, j in q:
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2**30:
                    rooms[I][J] = rooms[i][j] + 1
                    q += (I, J),