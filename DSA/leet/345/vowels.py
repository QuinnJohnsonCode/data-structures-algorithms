# vowels.py

'''
Given:
    - String s

Return:
    - String s with vowels reversed

Observations:
    - String is mixed characters (lower/upper)
    - Immediately lowercase the string to make it easier to work with
        - Second thought, do not do this because we need to return the exact sequence, with case in mind
        - Instead, lowercase when comparing

Implementation:
    - Have two pointers
        - One pointer starts at the beginning
        - One starts at the end
    - If a character is a vowel i.e in ['a', 'e', 'i', 'o', 'u']
        - Do not increment the pointer
    - If both pointers are vowels
        - Swap them
    - If a character is not a vowel
        - Increment the pointer

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1

        # Vowels list to check if a character is in it
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)

        while start < end:
            # Find the vowels first
            while start < end and s_list[start] not in vowels:
                start += 1
            
            while start < end and s_list[end] not in vowels:
                end -= 1


            if (start < end):
                # Swap
                temp = s_list[start]
                s_list[start] = s_list[end]
                s_list[end] = temp

                start += 1
                end -= 1

        return ''.join(s_list)



# Tests
sol = Solution()
assert sol.reverseVowels("IceCreAm") == "AceCreIm"
assert sol.reverseVowels("leetcode") == "leotcede"