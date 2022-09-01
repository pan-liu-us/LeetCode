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

var isBalanced = function(root) { 
    if (root === null) {
        return true;
    }
    if (isBalanced(root.left) && isBalanced(root.right)) {
        let left = root.left == null ? 1 : root.left.val;
        let right = root.right == null ? 1 : root.right.val;
        root.val = Math.max(left, right) + 1;
        return Math.abs(left - right) <= 1;
    }
    return false;
}
