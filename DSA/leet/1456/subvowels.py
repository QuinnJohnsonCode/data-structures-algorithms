# subvowels.py

'''

Given:
    - String s
    - Integer k

Return:
    - Maximum number of vowels in any substring of s with length k

Observations:
    - Very similar to max subarray problem
    - Sliding window solution should be used
    - Instead of summing up all values, we see if the current is a vowel
        - If it is, add one, if it isn't, don't add one
    - If the outside of our window is a vowel, we deduct one from our running total

'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0

        # Count up the first window
        for i in range(0, k, 1):
            let = s[i]

            count = count + 1 if let in vowels else count
        
        # Set the max_vowels to whatever the current counter is after the first window
        max_vowels = count

        # Count subsequent windows
        for i in range(k, len(s), 1):
            let = s[i]
            prev_let = s[i - k]

            # Increment count if the new letter is a vowel
            # Decrement count if the letter we lost was a vowel
            count = count + 1 if let in vowels else count
            count = count - 1 if prev_let in vowels else count

            # Set the new max_vowels if the count is better
            max_vowels = max(max_vowels, count)

        return max_vowels

# Tests
sol = Solution()
assert sol.maxVowels("abciiidef", 3) == 3
assert sol.maxVowels("aeiou", 2) == 2
assert sol.maxVowels("leetcode", 3) == 2