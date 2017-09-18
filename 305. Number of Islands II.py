class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = [];
        island = Union();
        for pos in positions:
            x, y = pos;
            island.add((x, y));
            for xi, yi in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xn, yn = x+xi, y+yi;
                if (xn,yn) in island.parent:
                    island.unite((x,y), (xn, yn));
            ans+=[island.count];
        return ans;
    

class Union():
    def __init__(self):
        self.parent = {};
        self.size = {}
        self.count = 0;
    
    def add(self, p):
        self.parent[p] = p
        self.size[p] = 1;
        self.count+=1;
    
    def find(self, p):
        while p!=self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]];
            p = self.parent[p];
        
        return p;
    
    def unite(self, p, q):
        p, q = self.find(p), self.find(q);
        if p==q:
            return;
        self.parent[p] = q;
        self.size[q]+=self.size[p];
        self.count-=1;
        