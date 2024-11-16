# equalrowcol.py

'''

Given:
    - 0-indexed n x n integer matrix grid

Return:
    - Number of pairs (ri, cj)
        - Such that row (ri) and column (cj) are equal

Concept:
    - A row and column pair are considered equal if
        - They contain the same elements in the same order (i.e an equal array)

Approach:
    - Ordering matters, thus cannot just sort and look for frequencies
    - Could store a set of lists for the columns and a set for the rows
        - Then iterate through the columns and see how many are in the rows
        - Duplicates wouldn't be counted though...
        - Could count the frequencies of these lists rather than simply 

        - On second thought, storing lists as the hash key is not doable
    - We have to think about what information we can hash
        - We could store a string containing the values of a row/column
        - So [2, 7, 7] would be "277"
        - This solves our hashing issue
    - List equality in python works, == will determine if the values/orderings are the same

'''

from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_hash = defaultdict(int)
        equal_pairs = 0
        n = len(grid)

        for row in grid:
            row_hash[tuple(row)] += 1
        
        print(row_hash)

        # n * m :(
        for i in range(n):
            col = tuple(grid[j][i] for j in range(n))
            equal_pairs += row_hash[col]

        return equal_pairs

# Tests
sol = Solution()
assert sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1
assert sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
assert sol.equalPairs([[11,1],[1,11]]) == 2