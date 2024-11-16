# product.py

'''

Given:
    - integer array nums

Return:
    - An array answer
        - answer[i] is equal to the product of all the elements of nums except nums[i]

Restrictions:
    - O(n) time
    - No divison operation

Observations:
    - Precompute values
    - Can loop through nums more than once and still maintain O(n)

'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [0] * len(nums)
        answer[0] = 1

        # Fill prefix
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]

        R = 1
        for i in range(len(nums) - 1, -1, -1):
            
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
        
# Tests
sol = Solution()
assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]