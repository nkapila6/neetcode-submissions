class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       mem = {}

       for i,n in enumerate(nums):
            if n in mem.keys():
                continue

            mem[n] = nums.count(n)
        
       vals = sorted(mem, key=mem.get, reverse=True)

       return vals[:k]




