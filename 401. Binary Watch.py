class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num==0:
            return ['0:00']
        def check(hour, l):
            check = [2**(i) for i in range(l-1, -1, -1)];
            result = 0
            for c in hour:
                result+=check[c];
            
            return result;
                
        
        result = []
        for h in range(min(5, num+1)):
            m = num-h;
            if m>6:
                continue;
            
            for hour in itertools.combinations(range(4), h):
                for minute in itertools.combinations(range(6), m):
                    hour_val = check(hour, 4);
                    minute_val = check(minute, 6);
                    if hour_val<12 and minute_val<60:
                        minute_str = str(minute_val) if minute_val>=10 else '0'+str(minute_val)
                        result.append(str(hour_val)+':'+minute_str);
        
        return result;
       


    def readBinaryWatch(self, num):
    return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]


    class Solution(object):
    def readBinaryWatch(self, n):
        
        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins > 59: return
            if not n:
                res.append(str(hours) + ":" + "0" * (mins < 10) + str(mins))
                return
            for i in range(idx, 10):
                if i < 4: 
                    dfs(n - 1, hours | (1 << i), mins, i + 1)
                else:
                    k = i - 4
                    dfs(n - 1, hours, mins | (1 << k), i + 1)
        
        res = []
        dfs(n, 0, 0, 0)
        return res