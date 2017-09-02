from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = defaultdict(dict);
        for (c1, c2), num in zip(equations, values):
            g[c1][c2] = float(num);
            g[c2][c1] = float(1.0/num);
        
        def dfs(target, tmp, visit):
            if not tmp in g:
                return 0;
            
            for c in g[tmp]:
                if c==target:
                    return g[tmp][c];
                if c not in visit:
                    val = dfs(target, c, visit+[c])
                    if val!=0:
                        return val*g[tmp][c];
            
            return 0;
    
        result = []
        for c1, c2 in queries:
            if not c1 in g or not c2 in g:
                result.append(-1.0);
            else:
                val = dfs(c2, c1, [c1]);
                result.append(val if val else -1.0)
        
        return result;
	
	
	def calcEquation(self, equations, values, queries):
		quot = collections.defaultdict(dict)
		for (num, den), val in zip(equations, values):
			quot[num][num] = quot[den][den] = 1.0
			quot[num][den] = val
			quot[den][num] = 1 / val
		for k, i, j in itertools.permutations(quot, 3):
			if k in quot[i] and j in quot[k]:
				quot[i][j] = quot[i][k] * quot[k][j]
		return [quot[num].get(den, -1.0) for num, den in queries]