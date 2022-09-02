# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach 2: Fast and Slow Pointer: Floyd's Cycle Detection Algorithm
# no cycle: the fast pointer will eventually reach the end, return false 
# has cycle: the fast runner will eventually meet the slow runner, return true

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True

        