class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parent = range(n)
        def find(x):
            return x if parent[x] == x else find(parent[x])
        def union(xy):
            x, y = map(find, xy)
            parent[x] = y
            return x != y
        return len(edges) == n-1 and all(map(union, edges))
		
	
	def validTree(self, n, edges):
		neighbors = {i: [] for i in range(n)}
		for v, w in edges:
			neighbors[v] += w,
			neighbors[w] += v,
		def visit(v):
			map(visit, neighbors.pop(v, []))
		visit(0)
		return len(edges) == n-1 and not neighbors