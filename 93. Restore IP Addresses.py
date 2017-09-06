class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = [];
        
        def dfs(tmp, left):
            #print 'start', tmp, left, result
            if not left:
                if len(tmp)==4:
                    result.append('.'.join(tmp));
                return;
            if len(tmp)>4:
                return;
            
            for i in range(0,min(len(left), 4)):
                val = i+1;
                if left[:val][0]=='0' and val>1:
                    continue;
                if int(left[:val])<256:
                    dfs(tmp+[left[:val]], left[val:]);
            
            return;
    
        if not s or len(s)>12:
            return result;
        dfs([], s);
        return result;


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.helper(ans, s, 4, [])
        return ['.'.join(x) for x in ans]
        
    def helper(self, ans, s, k, temp):
        if len(s) > k*3:
            return
        if k == 0:
            ans.append(temp[:])
        else:
            for i in range(min(3,len(s)-k+1)):
                if i==2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                self.helper(ans, s[i+1:], k-1, temp+[s[:i+1]])