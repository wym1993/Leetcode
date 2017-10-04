class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if not nums:
            return [];
        result = []
        if a!=0:
            mid = -b/(2.0*a);
            i, j = 0, len(nums)-1
            while i<=j:
                if abs(nums[i]-mid)>abs(nums[j]-mid):
                    result.append(self.func(a, b, c, nums[i]));
                    i+=1;
                else:
                    result.append(self.func(a, b, c, nums[j]));
                    j-=1;
        else:
            result = [self.func(a, b, c, x) for x in nums];
        
        if a>0 or (a==0 and b<0):
            return result[::-1];
        else:
            return result;
    
    def func(self, a, b, c, x):
        return a*x**2+b*x+c;