# compress.py

'''

Given: 
    - Array of characters chars

Return:
    - Length of the compressed array

Algorithm:
    - Begin with empty string s, for each group of consecutive repeating characters in chars:
        - If the group's length is 1, append the character to s
        - Otherwise, append the character followed by the group length
        - Group lengths that are 10 or longer will be split into multiple characters
            - ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
            - = ["a","b","1","2"] (one a followed by 12 b's)
    - Constant extra space (must modify original array)

Observations:
    - The final output array's length is going to be smaller or equal to the input
        - Gives us space to overwrite (maybe keep track of where we can overwrite?)
    - We always have to append a character once we see it for the first time
        - We may have to put a number after it

'''

class Solution:
    def compress(self, chars: list[str]) -> int:
        res = 0
        i = 0

        # Scan through each character
        while i < len(chars):

            # Initialize group_length to 1
            group_length = 1

            # Verify i + group_length is within bounds and check if the next character is the same character
            while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                group_length += 1
            
            # After the while loop, we've found the new character

            # Overwrite chars at res to the current character
            chars[res] = chars[i]
            res += 1

            # Overwrite the digits if more than one character was found
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)

            # Move i up by group_length digits
            i += group_length
        return res

# Tests
sol = Solution()
assert sol.compress(["a","a","b","b","c","c","c"]) == 6
assert sol.compress(["a"]) == 1
assert sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4
assert sol.compress(["a","b","c"]) == 3
assert sol.compress(["a","a","a","b","b","a","a"]) == 6
assert sol.compress(["a","a","a","a","a","b"]) == 3