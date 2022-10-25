# Approach 2: Two Pointers | Floyd's Cycle Finding Algorithm
# Time complexity : O(n)
# List has no cycle: depends on the list's length n, O(n)
# List has a cycle: depends on both non-cyclic length n and cyclic length m, 0(n+m)

# Space complexity : O(1)
# We only use two nodes, slow and fast

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
