class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = -1
        while i < j:
            length = min(heights[i], heights[j])
            width = j - i
            maxArea = max(length * width, maxArea)

            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return maxArea
    