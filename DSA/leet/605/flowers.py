# flowers.py

'''
- Some plots are planted/some not
    - Planted represented by 1
    - Empty represented by 0
- Cannot be placed in adjacent plots

Given:
    - integer array flowerbed
        - contain's 0's and 1's
        - 0 for empty, 1 for non empty
    - integer n

Return:
    - true if n new flowers can be planted
        - no violations of adjacent rule
    - false otherwise

Constraints:
    - 1 <= flowerbed.length <= 2 * 104
    - flowerbed[i] is 0 or 1.
    - There are no two adjacent flowers in flowerbed.
    - 0 <= n <= flowerbed.length

Goal:
    - Plant as many as possible
    - Plant up to n

Consequences of planting:
    - i - 1 and i + 1 can no longer be planted
    - If i - 1 is 

O(n) possible solution
    - Initial counter = 0
    - Go through the list, look left and right
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        flowerbed_length = len(flowerbed)
        count = 0
        for i in range(flowerbed_length):
            
            # If the flowerbed is already planted, no action can be taken
            if flowerbed[i] == 1:
                continue

            # Choice: To plant or not to plant
            if self.canPlant(flowerbed, i, flowerbed_length):
                flowerbed[i] = 1
                count += 1

            # Check to see if we've fulfilled the requirement where count == n
            if count == n:
                return True
                
        return False

    def canPlant(self, flowerbed: list[int], i: int, length: int) -> bool:
        if length == 1:
            return flowerbed[i] == 0
            
        if i == 0:
            return flowerbed[i + 1] == 0
        if i == length - 1:
            return flowerbed[i - 1] == 0
        
        return flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0
        


# Tests
sol = Solution()
assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False

