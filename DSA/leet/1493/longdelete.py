# longdelete.py

'''

Given:
    - Binary array nums

Return:
    - Size of the longest non-empty subarray containing only 1's
    - Return 0 if there is no such subarray
'''

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        
        max_ones = 0
        zeroes_in_window = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes_in_window += 1

            while (left <= right) and (zeroes_in_window > 1):
                if nums[left] == 0:
                    zeroes_in_window -= 1
                left += 1

            max_ones = max(max_ones, right - left)

        return max_ones

# Tests
sol = Solution()
assert sol.longestSubarray([1, 1, 0, 1]) == 3
assert sol.longestSubarray([0,1,1,1,0,1,1,0,1]) == 5
assert sol.longestSubarray([1,1,1]) == 2