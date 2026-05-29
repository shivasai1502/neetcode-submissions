class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            r = target - nums[i]
            if r in nums:
                j = nums.index(r)
                if i!=j:
                    return sorted([i, j])
        