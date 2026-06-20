class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mem, out = [], [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while mem and temp > temperatures[mem[-1]]:
                i = mem.pop()
                out[i] = idx - i
            mem.append(idx)

        return out
