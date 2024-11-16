# mid-node.py

'''

Given:
    - Head of linked list

Return:
    - Head of the modified linked list

Action:
    - Remove the middle node
        - Size n
        - floor(n / 2) (//)

'''


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# INITIAL SOLUTION 1 1/2 Iterations of the LL
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if head.next == None:
#             return None

#         # Get length of LL
#         n = 0
#         temp = head
#         while temp:
#             temp = temp.next
#             n += 1

#         mid = n // 2
#         node_before = head

        

#         for i in range(mid - 1):
#             node_before = node_before.next
        
#         node_after = node_before.next.next

#         node_before.next = node_after

#         return head

# EDITORIAL SOLUTION 1/2 Iterations of the LL
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next == None:
            return None
        
        # Two pointers (fast/slow)

        # Slow starts at beginning, head starts 2 nodes ahead
        slow = head
        fast = head.next.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches the end, slow contains the predecessor to the middle node
        slow.next = slow.next.next

        return head