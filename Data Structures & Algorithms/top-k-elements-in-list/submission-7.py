class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for freq, value in count.items():
            heapq.heappush(heap, (value, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

        