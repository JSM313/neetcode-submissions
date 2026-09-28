class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket_index = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in bucket_index:
                bucket_index[comp].append(index)
                return bucket_index[comp]
            else:
                bucket_index[num] = [index]
        return []
        