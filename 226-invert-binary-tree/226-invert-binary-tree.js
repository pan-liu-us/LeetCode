// Approach 2: Iterative BFS

// T.C. = O(n)
// n is the number of nodes in the tree, each node in the tree is visited / added to the queue only once

// S.C. = O(n)
// size of queue, worst case for a full binary tree, the leaf level has n/2 leaves

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
    if (!root) {
        return root;
    }
    
    let q = [];
    q.push(root);
    
    while (q.length) {
        let cur = q.shift();
        [cur.left, cur.right] = [cur.right, cur.left]
        
        if (cur.left) {
            q.push(cur.left);
        }
        if (cur.right) {
            q.push(cur.right);
        }
    }
    
    return root;
};
