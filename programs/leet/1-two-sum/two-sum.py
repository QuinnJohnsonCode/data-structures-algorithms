# Leetcode Problem 1
# "Two Sum"
# Solution by Quinn Johnson 7/15/23

def twoSum(nums: list[int], target: int) -> list[int]:
    indices = []
    # Put all nums in a dictionary with their index
    numsDict = {}
    for i in range(len(nums)):
        numsDict[nums[i]] = i

    # Loop through nums searching for the value that matches in dict
    for i in range(len(nums)):
        diff = target - nums[i]
        if (diff in numsDict and numsDict[diff] != i):
            indices = [i, numsDict[diff]]
            break
            
    return indices

# Acceptance Tests
assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
