# altitude.py

'''

Given:
    - Integer array gain of length n
    - gain[i] is the net gain in altitude between points i and i + 1

Return:
    - Highest altitude of a point

'''

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_altitude = 0
        altitude_sum = 0


        for i in range(len(gain)):
            altitude_sum += gain[i]
            max_altitude = max(altitude_sum, max_altitude)
        
        return max_altitude


# Tests
sol = Solution()
assert sol.largestAltitude([-5,1,5,0,-7]) == 1
assert sol.largestAltitude([-4,-3,-2,-1,4,3,2]) == 0