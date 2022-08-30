/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */

// Recursive Approach

var lowestCommonAncestor = function(root, p, q) {
  // base case
  if ((p.val > root.val && q.val < root.val) || (p.val < root.val && q.val > root.val)) {
    return root;
  }
  if (p === root || q === root) {
    return root;
  }
  
  // recursion
  // both the nodes p and q are in the right subtree
  if (p.val > root.val && q.val > root.val) {
    return lowestCommonAncestor(root.right, p, q);
  }
  
  // both the nodes p and q are in the left subtree
  if (p.val < root.val && q.val < root.val) {
    return lowestCommonAncestor(root.left, p, q);
  }
  
  return null;
};