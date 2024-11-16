# unique.py

'''

'''

from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hash_nums = defaultdict(int) # <num, occurrences>
        set_occurrences = set()

        for n in arr:
            hash_nums[n] = hash_nums[n] + 1

        for occurrences in hash_nums.values():
            if occurrences in set_occurrences:
                return False

            set_occurrences.add(occurrences)

        return True

# Tests
sol = Solution()
assert sol.uniqueOccurrences([1,2,2,1,1,3]) == True
assert sol.uniqueOccurrences([1,2]) == False
assert sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) == True