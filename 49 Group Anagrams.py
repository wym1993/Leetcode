class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return [];
        
        store = {};
        result = [];
        for str in strs:
            temp = "".join(sorted(str));
                
            if not temp in store:
                idx = len(result)
                store[temp] = idx;
                result.append([str]);
            else:
                idx = store[temp];
                result[idx].append(str);
        
        return result;