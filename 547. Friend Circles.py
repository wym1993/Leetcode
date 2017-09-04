
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parent = [i for i in range(len(M))];
        
        def find(x):
            return x if parent[x]==x else find(parent[x])
    
        def union(x, y):
            x, y = find(x), find(y);
            if x!=y:
                parent[x] = y;
        
        edges = []
        for i in range(len(M)):
            for j in range(i+1, len(M)):
                if M[i][j] == 1:
                    edges.append([i, j]);
        
        for edge in edges:
            union(edge[0], edge[1])
        #print parent
        return len([i for i in range(len(M)) if parent[i]==i])