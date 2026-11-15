class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res_set = set()
        for i in range(len(nums)):
            res_set.add(nums[i])
        if len(res_set) != len(nums):
            return True
        else:
            return False