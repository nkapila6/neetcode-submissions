class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return []

        memory = {}
        out = []

        for i in range(len(nums)):
            to_find = target-nums[i]

            if to_find in list(memory.keys()):
                return [memory[to_find], i]
            
            memory[nums[i]] = i