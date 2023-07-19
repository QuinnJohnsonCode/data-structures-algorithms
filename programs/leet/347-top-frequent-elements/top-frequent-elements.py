# Leetcode Problem 347
# "Top K Frequent Elements"
# Solution by Quinn Johnson 7/18/23

# Implementation
def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequency = {}
    elements = []

    # Fill map with frequencies
    for i in range(len(nums)):
        if (nums[i] in frequency):
            frequency[nums[i]] += 1
            continue
        frequency[nums[i]] = 1
    
    sortedFrequency = list(sorted(frequency.items(), key=lambda x:x[1], reverse=True))[:k]
    for i in sortedFrequency:
        elements.append(i[0])

    return elements


# Acceptance Tests
assert topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert topKFrequent([1], 1) == [1]