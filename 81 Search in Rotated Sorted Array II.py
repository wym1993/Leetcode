class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left=0; right=len(A)-1
        while left<=right:
            mid=(left+right)/2
            if A[mid]==target: return True
            if A[left]==A[mid]==A[right]:
                left+=1; right-=1
            elif A[left]<=A[mid]:
                if A[left]<=target<A[mid]: right=mid-1
                else: left=mid+1
            else:
                if A[mid]<=target<A[left]: left=mid+1
                else:right=mid-1
        return False