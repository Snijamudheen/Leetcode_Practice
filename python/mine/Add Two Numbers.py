'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

# This defines what a single node in the linked list looks like
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # The digit
        self.next = next      # Pointer to the next node

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to build the result linked list
        dummy = ListNode()
        current = dummy       # Pointer to the current node we're working on
        carry = 0             # Keeps track of carry-over when sum > 9

        # Keep looping as long as there's something in l1 or l2 or carry is not 0
        while l1 or l2 or carry:
            # Get values from current nodes, or 0 if the list is done
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0

            # Add the two digits plus any carry from before
            total = val1 + val2 + carry

            # Update carry for next time (e.g. 15 -> carry = 1)
            carry = total // 10

            # Create a new node with the digit part (e.g. 15 -> use 5)
            current.next = ListNode(total % 10)

            # Move the current pointer forward
            current = current.next

            # Move to the next nodes in the input lists, if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the list starting after the dummy node
        return dummy.next

#---------------------------------------------------------------------------------------------------------------

# if it is not in reverse order


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []

        # Push all nodes to stacks
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        result = None

        # Pop from stacks and add digits
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            node = ListNode(total % 10)

            # Insert at the front of the result list
            node.next = result
            result = node

        return result
