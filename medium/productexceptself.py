class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        opt=[1 for i in range(l)]
        pref=1
        suff=1
        for i in range(l):
            opt[i]*=pref
            pref=pref*nums[i]


        for i in range(l-1,-1,-1):
            opt[i]*=suff
            suff*=nums[i]


        return opt