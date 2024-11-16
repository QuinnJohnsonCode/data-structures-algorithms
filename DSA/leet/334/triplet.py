# triplet.py

'''

Given:
    - Integer array nums

Return:
    - True if there exists a triple of indices (i, j, k)
        - Such that i < j < k
        - and nums[i] < nums[j] < nums[k]
    - False if no such indices exist

Observations:
    - Greedy problem, thus a greedy choice exists
    - Can be O(n) time and O(1) space
'''

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        i_store = 2**31 - 1
        j_store = 2**31 - 1
        for i in range(len(nums)):
            # Check if nums[i] < i_store
            if nums[i] <= i_store:
                i_store = nums[i]
                continue

            # Check if nums[i] < j_store
            if nums[i] <= j_store:
                j_store = nums[i]
                continue
            
            return True

            
        return False

# Tests
sol = Solution()
assert sol.increasingTriplet([1, 2, 3, 4, 5]) == True
assert sol.increasingTriplet([5, 4, 3, 2, 1]) == False
assert sol.increasingTriplet([2, 1, 5, 0, 4, 6]) == True
assert sol.increasingTriplet([20, 100, 10, 12, 5, 13]) == True
assert sol.increasingTriplet([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == False