class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        store = {};
        result = [];
        for string in strings:
            index = len(result);
            for key in store.keys():
                if len(key)==len(string) and len(set([(ord(a)-ord(b))%26 for (a,b) in zip(string, key)]))==1:
                    index = store[key];
                    break;
            
            if index==len(result):
                result.append([string])
                store[string] = index;
            else:
                result[index].append(string);
        
        return result;