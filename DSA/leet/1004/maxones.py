# maxones.py

'''

Given:
    - Binary array nums
    - Integer k
    
Return:
    - Maximum number of consecutive 1's in the array if you can flip at most k 0's

Observations:
    - Can flip k 0's
        - We see a 0, choose to flip or not to flip
    - Sliding window
        - We only have control over k 0's
        - A 0 turning to a 1 will not only add one to a counter, it could connect two or more one's to many more
    - We need a way of counting consecutive 1's
        - Reading left to right for consecutive
    - Hint 1: Only flip a zero if it extends an existing window of 1's
    - Hint 2: In any given window, we can never have > K zeroes
        - Every window will contain the 1's and <= k zeroes
    - Hint 3: Not a fixed window size, can grow/shrink depending on the number of zeros
        - We don't have to flip the zeroes here
    - Hint 4:
        - The way to shrink or expand a window would be based on the number of zeroes that can be flipped
'''

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_ones = 0

        zeroes_in_window = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes_in_window += 1

            # Shrink the window
            while (left <= right and zeroes_in_window > k):
                if nums[left] == 0:
                    zeroes_in_window -= 1
                
                left += 1
            
            max_ones = max(max_ones, right - left + 1)

        return max_ones

# Tests
sol = Solution()

sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
assert sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
assert sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10