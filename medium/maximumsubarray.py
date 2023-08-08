class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=len(nums)
        mx=-10001
        cr=0


        for i in nums:
            if cr<0:
                cr=0
            cr+=i
            mx=max(mx,cr)

        return mx

                
            
        

        return mx