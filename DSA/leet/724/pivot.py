# pivot.py

'''

Given:
    - Integer array nums

Return:
    - Leftmost pivot index
    - If no index exists, return -1

Concept:
    - Pivot index is the index is where
        - The sum of all numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right
    - If the index is on the left edge, the left sum is 0 (vice versa for right edge)

Observations:
    - Set up left and right prefix sum arrays
    - left will contain the sum of all integers to the left of any index
    - right will contain the sum of all integers to the right of the index

'''

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_nums = sum(nums)
        
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == sum_nums - left_sum - nums[i]:
                return i

            left_sum += nums[i]
        return -1


# Tests
sol = Solution()

assert sol.pivotIndex([1,7,3,6,5,6]) == 3
assert sol.pivotIndex([1,2,3]) == -1
assert sol.pivotIndex([2,1,-1]) == 0