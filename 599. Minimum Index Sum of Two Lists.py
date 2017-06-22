class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = [];
        min_result = len(list1)+len(list2);
        for i1, rest1 in enumerate(list1):
            if rest1 in list2:
                if i1+list2.index(rest1)<min_result:
                    min_result = i1+list2.index(rest1)
                    result = [rest1];
                elif i1+list2.index(rest1)==min_result:
                    result.append(rest1);
        
        return result;