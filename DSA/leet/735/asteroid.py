# asteroid.py

'''

Given:
    - Integer array asteroids representing asteroids in a row

Concept:
    - Each asteroid:
        - Absolute value represents its size
        - Sign represents its direction (positive right, negative left)
        - Moves at the same speed
    - If two asteroids meet
        - The smaller one will explode
        - If both are the same size
            - Both will explode
    - Two asteroids moving in the same direction will never meet

Task:
    - Find out the state of the asteroids after all collisions

Return:
    - List of asteroids after all collisions have been handled

Approach:
    - Two asteroids moving in the same direction will never meet
    - Stack based solution
    - Two stacks?
    - Keep one stack for asteroids moving to the left, one for those moving to the right
    - Update each stack for every collision
        - If the current value is positive (moving to the right)
            - Go to the left stack and compare, if the current is bigger
                - Pop the left stack
                - Push onto the right stack
            - Same: Pop and do nothing
            - Else
                - Do nothing
        - If the currnet value is negative (moving to the left)
            - Go to the right stack and compare, if the current is bigger
                - Pop the right stack
                - Push onto the left stack
            - Same: Pop and do nothing
            - Else
                - Do nothing

    - At the end, only one stack should be full?
    - Return the stack that still has elements (or none in the case that all asteroids cancelled each other out)
'''

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            flag = False

            # Loop while the stack is not empty and there are collisions
            while len(stack) > 0 and (stack[-1] > 0 and asteroid < 0):
                top = stack[-1]

                # If the current asteroid is larger than the top, pop and continue
                if abs(top) < abs(asteroid):
                    stack.pop()
                    continue

                # If the current asteroid is equal, just pop
                elif abs(top) == abs(asteroid):
                    stack.pop()

                # If this is reached, the current asteroid was either equal or smaller than the top
                # In this case, we should not append the asteroid
                flag = True
                break
            
            # If the flag has not changed, we can append the current asteroid
            if not flag:
                stack.append(asteroid)
            
        return stack


# Tests
sol = Solution()
assert sol.asteroidCollision([5, 10, -5]) == [5, 10]
assert sol.asteroidCollision([8, -8]) == []
assert sol.asteroidCollision([10,2,-5]) == [10]
assert sol.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
assert sol.asteroidCollision([-2,-2,1,-1]) == [-2,-2]
assert sol.asteroidCollision([1,-2,-2,-2]) == [-2, -2, -2]