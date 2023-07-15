# Leetcode Problem 217
# "Contains Duplicate"
# Solution by Quinn Johnson 7/15/23

def containsDuplicate(nums: list[int]) -> bool:
    setOfNumbers = set()
    
    # Insert num into dictionary as key
    for i in range(len(nums)):
        if (nums[i] in setOfNumbers):
            return True
        setOfNumbers.add(nums[i])
    return False


# Acceptance Tests
assert containsDuplicate([1,2,3,1]) == True
assert containsDuplicate([1,2,3,4]) == False
assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True