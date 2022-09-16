// Approach 1: Recursion

// Time complexity: O(N)
// N is a number of nodes in the tree, since one visits each node exactly once.

// Space complexity: O(N)
// In the worst case of completely unbalanced tree, to keep a recursion stack.

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if (!p && !q) {
        return true;
    }
    if (!p || !q) {
        return false
    }
    if (p.val !== q.val) {
        return false;
    }
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};