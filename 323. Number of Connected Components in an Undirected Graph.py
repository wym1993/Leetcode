import collections
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        def dfs(visit, g, i):
            if visit[i]:
                return;
            visit[i] = True;
            for n in g[i]:
                dfs(visit, g, n);
            
            return;
        
        visit = [False for _ in range(n)];
        g = collections.defaultdict(list);
        for edge1, edge2 in edges:
            g[edge1].append(edge2);
            g[edge2].append(edge1);
        
        res = 0;
        for i in range(n):
            if not visit[i]:
                dfs(visit, g, i);
                res+=1;
        
        return res
		

from collections import defaultdict
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        g = {x:[] for x in xrange(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ret = 0
        for i in xrange(n):
            queue = [i]
            ret += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return ret