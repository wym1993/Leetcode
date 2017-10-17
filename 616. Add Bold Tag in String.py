class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if not dict:
            return s;
        store = [];
        cands = set([len(word) for word in dict])
        for i in range(len(s)-min(cands)+1):
            for cand in cands:
                if s[i:i+cand] in dict:
                    store.append([i, i+cand]);
        
        if not store:
            return s;
        store.sort();
        
        start, end = store[0][0], store[0][1];
        res = s[:start];
        for x, y in store[1:]:
            if x<=end:
                start, end = min(start, x), max(end, y);
            else:
                res+='<b>'+s[start:end]+'</b>'+s[end:x];
                start, end = x, y;
        
        res+='<b>'+s[start:end]+'</b>'+s[end:];
        return res;