# decode.py

'''

Given:
    - Encoded String

Return:
    - Decoded String

Encoding Rule:
    - k[encoded_string], where encoded_string inside the square brackets is being repeated exactly k times
        - k is guaranteed to be a positive integer

Assumptions:
    - Input string is always valid
    - No extra white spaces
    - Square brackets are well-fromed
    - Original data does not contain any digits and that digits are only for those repeat numbers, k
        - Ex. There will not be input like 3a or 2[4]

Approach:
    - Stack
    - Recursion?
    - Solve the square brackets recursively
    - ([) (]) (int) (non-int) <- Controls
        - If we see a left square bracket we start adding all values to the stack
        - If we see a right, we start popping and building up the new string

'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                
                
                # Collect temporary string within square brackets
                t_str = ""
                while stack and stack[-1] != "[":
                    t_str = stack.pop() + t_str

                # Pops "["
                stack.pop()


                # Collect integer to multiply string by
                t_int = ""
                while stack and stack[-1].isdigit():
                    t_int = stack.pop() + t_int
                
                stack.append(int(t_int) * t_str)
                continue

            stack.append(c)
        
        return "".join(stack)

# Tests
sol = Solution()
assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
assert sol.decodeString("3[a2[c]]") == "accaccacc"
assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
assert sol.decodeString("abc3[cd]xyz") == "abccdcdcdxyz"