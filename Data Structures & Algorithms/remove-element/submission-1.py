class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        count = 0
        for num in nums:
            if num != val:
                res.append(num)

        for i, num in enumerate(res):
            nums[i] = num
            count += 1
        
        return count
