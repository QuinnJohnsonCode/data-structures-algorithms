# water.py

'''

Given:
    - Integer array height of length n

Return:
    - Maximum amount of water a container can store

Concept:
    - n vertical lines drawn such that
        - Two endpoints of the ith line are (i, 0) and (i, height[i])
    - Find two lines that together with the x-axis form a container such that
        - The container contains the most water
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height) - 1

        # Stores the maximum amount of water seen
        max_water = 0

        while start < end:
            height_start = height[start]
            height_end = height[end]

            water = self.calculateWater(height_start, height_end, start, end)
            
            if water > max_water:
                max_water = water

            # Choose to move start or end
            if height_start < height_end:
                start += 1
            elif height_end < height_start:
                end -= 1
            else:
                start += 1
                end -= 1
        
        return max_water


    def calculateWater(self, height_start: int, height_end: int, start, end) -> int:
        return min(height_start, height_end) * (end - start)

# Tests
sol = Solution()
assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert sol.maxArea([1,1]) == 1
assert sol.maxArea([1,2,1]) == 2
assert sol.maxArea([1,3,2,5,25,24,5]) == 24