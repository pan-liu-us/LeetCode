// Approach 1: Depth-First Search

// Time Complexity: O(N) 
// N is the number of nodes in the given tree.

// Space Complexity: O(N)

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isUnivalTree = function(root) {
    var dfs = function(node, val) {
        if (node === null) {
            return true;
        }
        if (node.val !== val) {
            return false;
        }
        return dfs(node.left, val) && dfs(node.right, val)
    }
    return dfs(root, root.val)
};