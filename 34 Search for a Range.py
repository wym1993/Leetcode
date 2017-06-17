class Solution:
# @param A, a list of integers
# @param target, an integer to be searched
# @return a list of length 2, [index1, index2]
def searchRange(self, arr, target):
    start = self.binary_search(arr, target-0.5)
    if arr[start] != target:
        return [-1, -1]
    arr.append(0)
    end = self.binary_search(arr, target+0.5)-1
    return [start, end]

def binary_search(self, arr, target):
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start+end)//2
        if target < arr[mid]:
            end = mid
        else:
            start = mid+1
    return start

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = [];
        for i,num in enumerate(nums):
            if num==target:
                tmp.append(i);
        
        tmp.sort();
        if not tmp:
            return [-1, -1];
        elif len(tmp)==1:
            return [tmp[0], tmp[0]]
        else:
            return [tmp[0], tmp[-1]]