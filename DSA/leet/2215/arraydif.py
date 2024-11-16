# arraydif.py

'''

Given:
    - Two 0-indexed arrays nums1 and nums2

Return:
    - A list answer of size 2 where,
        - answer[0] is a list of all distinct integers in nums1 which are not present in nums2
        - answer[1] is a list of all distinct integers in nums2 which are not present in nums1

'''

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        answer = [set(), set()]
        for num in nums1:
            if num not in set_nums2 and num not in answer[0]:
                    answer[0].add(num)
        
        for num in nums2:
            if num not in set_nums1 and num not in answer[1]:
                answer[1].add(num)

        return [list(answer[0]), list(answer[1])]

    
# Tests
sol = Solution()

assert sol.findDifference([1,2,3], [2,4,6]) == [[1, 3], [4, 6]]
assert sol.findDifference([1,2,3,3], [1,1,2,2]) == [[3], []]