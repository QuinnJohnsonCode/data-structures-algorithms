# stars.py

'''

Given:
    - String s which contains stars *

Concept:
    - One operation you can
        - Choose a star in s
        - Remove the closest non-star character to its left as well as remove the star itself

Return:
    - String after all stars have been removed

'''

class Solution:
    def removeStars(self, s: str) -> str:
        remove_list = []

        for let in s:
            # pop
            if let == "*":
                remove_list.pop()
                continue

            # push
            remove_list.append(let)

        return "".join(remove_list)

# Tests
sol = Solution()
assert sol.removeStars("leet**cod*e") == "lecoe"
assert sol.removeStars("erase*****") == ""