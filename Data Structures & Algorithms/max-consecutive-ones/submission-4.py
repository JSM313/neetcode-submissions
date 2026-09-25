class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxnum = 0
        counter = 0

        for num in nums:
            if num == 1:
                counter += 1
                if counter > maxnum:
                    maxnum = counter
            else:
                counter = 0
        return maxnum
        