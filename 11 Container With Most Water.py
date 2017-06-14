class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0;
        right = len(height)-1;
        ans = 0;
        while left<right:
            if height[left]<height[right]:
                tmp = height[left]*(right-left);
                left+=1;
            else:
                tmp = height[right]*(right-left)
                right-=1;
            
            ans = max(ans, tmp);
        
        return ans