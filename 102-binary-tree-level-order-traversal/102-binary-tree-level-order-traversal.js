// Approach: Iteration
// Time complexity: O(N) each node is processed exactly once
// Space complexity: O(N) keep the output structure which contains N node values

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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    let res = []
    
    if (root === null) {
        return res
    }
    
    let q = [root,]
    
    while (q.length !== 0) {
        let level = [];
        let len = q.length;
        for (let i = 0; i < len; i++) {
            let node = q.shift();
            level.push(node.val);
            if (node.left) {
                q.push(node.left);
            }
            if (node.right) {
                q.push(node.right);
            }
        }
        res.push(level);
    }
    return res;
};