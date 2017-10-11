class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        status = {}
        
        def dfs(current, player, rnd):
            print current, player, rnd, not player
            if current in status.keys():
                return status[current];
            l = len(current);
            for i in range(l-1):
                if current[i:i+2] == '++':
                    result = dfs(current[:i]+'--'+current[i+2:], abs(player-1), rnd+1);
                    #print current[:i]+'--'+current[i+2:], result
                    status[current] = result
                    if result:
                        return True;
            
            #print player
            
            return True if not player else False;
            
        return dfs(s, 1, 0)