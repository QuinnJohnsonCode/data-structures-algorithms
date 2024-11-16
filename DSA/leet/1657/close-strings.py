# close-strings.py

'''

Given:
    - Two strings word1 and word2

Return:
    - True if word1 and word2 are close
    - False otherwise

Concept:
    - Strings are considered close if you can attain one from the other using
        - Operation 1:
            - Swap any two existing characters (eg. abcde -> a<e>cd<b>)
        - Operation 2:
            - Transform every occurrence of one existing character into another !!existing!! character
            - Do the same with the other character
            - (eg. aacabb -> bbcbaa) (all a's turn into b's and all b's turn into a's)

Approach:
    - Use hashset to count the frequency of each character in word1
    - Do the same for word2
    - If a character in word1 matches the frequency required for word2
        - We know that character is covered
    - If it does not match
        - Check to see if there is an unused character that has the required frequency but is not used in word2
        - This is required to be another existing character
            - This allows for a transform
        - Swap their frequency key values if one is found
            - If not, return False
    - Immediately rule out if lengths are not equal
        - No amount of swapping or transforming will cause the lengths to be the same
'''

from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        hash1 = self.getFrequency(word1)
        hash2 = self.getFrequency(word2)

        if set(hash1.keys()) != set(hash2.keys()):
            return False

        return sorted(hash1.values()) == sorted(hash2.values())
                    



    def getFrequency(self, word) -> dict:
        return defaultdict(int, {c: word.count(c) for c in set(word)})

# Tests
sol = Solution()
assert sol.closeStrings("abc", "bca") == True
assert sol.closeStrings("a", "aa") == False
assert sol.closeStrings("cabbba", "abbccc") == True
assert sol.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff") == False
assert sol.closeStrings("zwmqwwwcqwwqcqqcqqccqqcmqccqqqqccqqqwqqqqqcqwqm", "xhchhcxhhhhrcxhhxxchcxhhchrhhcxhcxhxrhhhhhhxhex") == False
assert sol.closeStrings("kmihff", "kffmmi") == False