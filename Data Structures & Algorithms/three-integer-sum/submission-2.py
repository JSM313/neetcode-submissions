class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort() # sorting the array.

        # Looping the array 
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue #This is to avoid duplicate results getting skipped. 

            l = index + 1 
            r = len(nums) - 1
            while l < r:
                three_sum = value + nums[l] + nums[r]

                # If the result is more than 0 
                if three_sum > 0:
                    r -= 1
                
                # Or if the vale is less than 0 
                elif three_sum < 0:
                    l += 1

                # Otherwise
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
            

        