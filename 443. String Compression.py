class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0;
        
        i = 0;
        while i<len(chars):
            c, cnt, i = chars[i], 1, i+1;
            while i<len(chars) and chars[i]==c:
                cnt+=1;
                del chars[i]
            
            if cnt>1:
                while cnt>0:
                    chars.insert(i, str(cnt%10));
                    cnt/=10;
                i+=1;
        
        return len(chars);