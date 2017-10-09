class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = collections.defaultdict(list);
        for edge in edges:
            tree[edge[0]].append(edge[1]);
            tree[edge[1]].append(edge[0]);
        
        while len(tree.keys())>2:
            leaves = [l for l in tree.keys() if len(tree[l])==1];
            for leaf in leaves:
                tree[tree[leaf][0]].remove(leaf);
                del tree[leaf];
        
        return tree.keys() if tree.keys() else [0]