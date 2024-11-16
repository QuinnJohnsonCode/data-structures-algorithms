# max-twin-sum.py

'''

Given:
    - Linked List of size n
    - Head of linked list with even length

Return:
    - The maximum twin sum of the LL

Concept:
    - Where n is even
        - The ith node (0-indexed) of the LL is known as the twin of the (n - 1 - i)th node
            - if 0 <= i <= (n / 2) - 1
    - Twin Sum: Sum of a node and its twin

Approach:
    - Stack
    - Two Pointers
        - One pointing at the twin node??
        - One pointing at the current node?

'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# First solution, O(n) time, O(n) space
# Not great, could be improved by losing the stack making O(1) space
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []

        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next

        max_val = 0
        n = len(stack) // 2
        for i in range(n):
            max_val = max(max_val, stack[i] + stack[n - i - 1])
        
        return max_val

# Optimized soluton, O(n) time, O(1) space
# Get middle node, reverse the list after the middle node, add up values between head and prev
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find middle node
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse LL (store in prev)
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Find max twin sum between reversed list and forward list
        max_val = 0
        while head and prev:
            max_val = max(max_val, head.val + prev.val)
            head = head.next
            prev = prev.next

        return max_val