class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def dfs(nums1, nums2, k):
            if not nums1:
                return nums2[k];
            if not nums2:
                return nums1[k];
            i1, i2 = len(nums1)/2, len(nums2)/2;

            if i1+i2<k:
                if nums1[i1]<nums2[i2]:
                    return dfs(nums1[i1+1:], nums2, k-i1-1);
                else:
                    return dfs(nums1, nums2[i2+1:], k-i2-1);
            else:
                if nums1[i1]<nums2[i2]:
                    return dfs(nums1, nums2[:i2], k);
                else:
                    return dfs(nums1[:i1], nums2, k);

        m, n = len(nums1), len(nums2);
        if (m+n)%2==1:
            return dfs(nums1, nums2, (m+n)/2)
        else:
            return (dfs(nums1, nums2, (m+n)/2)+dfs(nums1, nums2, (m+n)/2-1))/2.0;
    
        