class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        stack = [] 

        for index, temp in enumerate(nums):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex  = stack.pop()
                res[stackIndex] = (index - stackIndex)
            stack.append([temp, index])
        return res