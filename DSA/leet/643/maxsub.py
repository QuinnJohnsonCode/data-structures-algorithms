# maxsub.py

'''

Given:
    - Integer array nums with n elements
    - Integer k

Return:
    - Maximum average value of subarray where length = k
    - Calculation error must be less than 10^-5 (float rounding)

Observations:
    - Subarray suggesting sliding window
    - Have a start and end point on each iteration, move them up by k
    - Take the average of the positions in that window

'''

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sums = sum(nums[0:k])
        max_sum = sums
        
        for i in range(k, len(nums), 1):
            sums = sums + nums[i] - nums[i - k]
            max_sum = max(max_sum, sums)
            
        return max_sum / k


# Tests
sol = Solution()
sol.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75
sol.findMaxAverage([5], 1) == 5.0

sol.findMaxAverage([0,1,1,3,3], 4)