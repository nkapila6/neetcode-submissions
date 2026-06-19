class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # list of int nums
        l = len(nums)
        out = [1]*l

        # let's try brute force O(n*m) for now
        for i,val in enumerate(nums):
            arr = [nums[j] for j in range(len(nums)) if i != j]
            for v in arr:
                out[i] *= v

        return out
