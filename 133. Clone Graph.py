# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node;
    
        root = UndirectedGraphNode(node.label);
        stack = [node]
        visited = {node.label:root};
        while stack:
            top = stack.pop();
            
            for n in top.neighbors:
                if n.label not in visited:
                    stack.append(n)
                    visited[n.label] = UndirectedGraphNode(n.label)
                visited[top.label].neighbors.append(visited[n.label])
        
        return root;