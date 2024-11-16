# oddeven.py

'''

Given:
    - Head of singly linked list

Return:
    - Return the reordered list

Task:
    - Group all nodes with odd indices together followed by the nodes with even indices
    - First node is considered odd, and the second node is even and so on
    - Relative order inside both the even and odd groups should remain
    - O(1) Space and O(N) Time

    

'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if list is of 0 or 1 elements
        if not head or not head.next:
            return head


        # Initialize pointers for odd and even nodes
        odd = head
        even = head.next
        even_head = even  # Save the start of the even list to attach it later
        
        # Traverse the list and rearrange odd and even nodes
        while even and even.next:
            odd.next = even.next
            odd = odd.next  # Move the odd pointer
            even.next = odd.next
            even = even.next  # Move the even pointer
        
        # After finishing the traversal, link the last odd node to the head of the even list
        odd.next = even_head

        return head