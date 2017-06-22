class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        result = 0;
        min_num = arrays[0][0];
        max_num = arrays[0][-1];
        for i in range(1, len(arrays)):
            result = max(result, abs(max_num-arrays[i][0]), abs(min_num-arrays[i][-1]))
            min_num = min(arrays[i][0], min_num);
            max_num = max(arrays[i][-1], max_num);
        
        return result;
                