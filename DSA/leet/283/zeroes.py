# zeroes.py

'''

Given:
    - Integer array nums

Objective:
    - Move all 0's to the end of the array while mainting the relative order of non-zero elements
    - Do it in place, no copy of the array (O(1) space)

Observations:
    - If the length of nums is 1, do nothing
    - Must swap the values of the two positions
    - Two pointers
        - One initially points to the beginning
        - 

'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0
        overwrite = 0
        for i in range(len(nums)):
            curr = nums[i]
            
            if curr == 0:
                count += 1
                continue
            
            nums[overwrite] = curr
            overwrite += 1
        
        nums[-count:] = [0] * count
        print(nums)

# Tests
sol = Solution()

sol.moveZeroes([0,1,0,3,12])
sol.moveZeroes([0])