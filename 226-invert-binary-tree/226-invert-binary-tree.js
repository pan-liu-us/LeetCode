// Approach 1: Recursive DFS

// T.C. = O(n)
// n is the number of nodes in the tree, each node is visited once

// S.C. = O(h) => O(n)
// h is the height of the tree, because of recursion, O(h) function calls will be placed on the stack in the worst case

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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (root === null) {
        return null;
    }
    // swap children
    let temp = root.right;
    root.right = root.left;
    root.left = temp;

    // invert child trees
    invertTree(root.right);
    invertTree(root.left);

    return root;
};