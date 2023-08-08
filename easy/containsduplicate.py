class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length= len(nums)
        nums.sort()
        for i in range(1,length):
            if nums[i-1]==nums[i]:
                return True
        return False