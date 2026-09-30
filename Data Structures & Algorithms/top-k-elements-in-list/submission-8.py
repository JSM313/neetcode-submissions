class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)] #we need a list equal to the len of nums. 

        for value, count in count.items():
            freq[count].append(value) #each index will basically define how many times each number appeared.
        
        # Now since there we have to find the most frequent they will be inserted at the last.
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res
                

        