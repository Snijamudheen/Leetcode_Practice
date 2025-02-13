# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val  # Store value of the node
#         self.next = next  # Pointer to the next node in the list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # None   1 -> 2 -> 3 -> 4 -> 5
        # prev curr  temp

        # None <- 1     2 -> 3 -> 4 -> 5
        # prev  curr   temp = curr.next

        # None <- 1     2 -> 3 -> 4 -> 5
        #        prev  temp
        #              curr

        # Initialize pointers
        curr = head  # Start at the head of the list
        prev = None  # Previous node starts as None since first node will become last

        while curr:  # Loop until we reach the end of the list
            temp = curr.next  # Store the next node
            curr.next = prev  # Reverse the pointer to point to the previous node
            prev = curr  # Move prev one step forward (to current node)
            curr = temp  # Move curr one step forward (to stored next node)

        return prev  # Return new head (previously the last node)
