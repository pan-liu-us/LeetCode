# Approach 1: Hash Set

# Time complexity: O(n)
# We visit each of the n elements in the list at most once. 
# Adding a node to the hash table costs only O(1) time.

# Space complexity: O(n)
# At most n elements can be added to the hash set.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()

        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next

        return False
