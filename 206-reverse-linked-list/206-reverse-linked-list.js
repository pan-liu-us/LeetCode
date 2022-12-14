// Approach: Iterative
// Time complexity : O(n)
// Space complexity : O(1)

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let prev = null;
    let curr = head;
    while (curr) {
        next_temp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next_temp;
    }
    return prev;   
};