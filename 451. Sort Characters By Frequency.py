from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = "";
        store = Counter(s);
        for ele, count in store.most_common(len(store)):
            result+=ele*count
        
        return result;