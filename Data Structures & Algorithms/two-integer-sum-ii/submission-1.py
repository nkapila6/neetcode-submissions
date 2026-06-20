class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers)-1

        while 1:
            summed = numbers[first]+numbers[last]
            if summed == target:
                break
            if summed > target:
                last-=1
            elif summed < target:
                first+=1

        return [first+1, last+1]