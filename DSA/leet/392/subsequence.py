# subsequence.py

'''

Given:
    - Two strings s and t

Return:
    - True if s is a subsequence of t
    - False otherwise

Concept:
    - Subsequence of a string is a new string that is formed from the orginal string by deleting soem of the characters
    - This is without altering the relative positions

Implementation:
    - Two pointer solution
    - One is tracking the characters in s, the other is tracking characters in t
    - If the t pointer equals the value of the s pointer, move the s pointer up
    - Always move the t pointer up
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If len(s) > len(t), s could not be a subsequence of t
        if len(s) > len(t):
            return False

        # If s equals t, then s is a subsequence of t        
        if s == t:
            return True

        j = 0 # Tracks the position in s
        for i in range(len(t)):
            # i will track the position in t

            # If we've seen every character in j, we've found s is a subsequence of t
            if j >= len(s):
                return True

            # Same character, increment j
            if t[i] == s[j]:
                j += 1

            

        return j >= len(s)

# Tests
sol = Solution()
assert sol.isSubsequence("abc", "ahbgdc") == True
assert sol.isSubsequence("axc", "ahbgdc") == False