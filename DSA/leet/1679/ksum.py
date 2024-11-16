# ksum.py
from collections import defaultdict

'''

Given:
    - Integer array nums
    - Integer k

Return:
    - Maximum number of operations you can perform on the array

Concept:
    - One operation
        - Pick two numbers from the array whose sum equals k and remove them from the array

Observations:
    - We know this is some sort of two pointer problem
        - Not yet seeing where two pointers come into it
    - Hash map for quick lookup of valid answer for any index
        - <key, value> = <number, [indexes]>
        - A number can have more than one index, indexes however will be sorted in ascending order
    - Choice at any index is to either remove or keep
        - Removing at every available index may lead to a less than maximum solution
        - Also not seeing why this may be true? Is there a time where removing one element will not allow another to sum up?
    

'''

# O(n log n) Time (uses sorting) with O(1) space complexity
# class Solution:
#     def maxOperations(self, nums: list[int], k: int) -> int:
#         # Sort the array
#         nums.sort()

#         operations = 0
#         start = 0 
#         end = len(nums) - 1

#         while (start < end):
#             sums = nums[start] + nums[end]

#             if sums == k:
#                 start += 1
#                 end -= 1
#                 operations += 1
#                 continue
            
#             if sums < k:
#                 start += 1
#                 continue
            
#             if sums > k:
#                 end -= 1

#         return operations

# O(n) Time Complexity with O(n) space complexity
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        operations = 0
        nums_hash = {} # <key, value> = <nums[i], freq>


        for i in range(len(nums)):
            curr = nums[i]
            target = k - curr

            if target in nums_hash and nums_hash[target] > 0:
                nums_hash[target] = nums_hash[target] - 1
                operations += 1
            else:
                if curr not in nums_hash:
                    nums_hash[curr] = 1
                else:
                    nums_hash[curr] = nums_hash[curr] + 1

        return operations

# Tests
sol = Solution()
assert sol.maxOperations([1, 2, 3, 4], 5) == 2
assert sol.maxOperations([3, 1, 3, 4, 3], 6) == 1
assert sol.maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2) == 2