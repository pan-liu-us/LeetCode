// Approach: Breadth First Search
// Time complexity: O(N)
// Space complexity: O(N)


/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
    if (node === null) {
        return null;
    }
    
    let visited = new Map();
    let q = [node];
    visited.set(node, new Node(node.val, [])) ;
    
    // BFS
    while (q.length > 0) {
        let cur = q.shift();
        for (let nei of cur.neighbors) {
            if (!visited.has(nei)) {
                visited.set(nei, new Node(nei.val, []));
                q.push(nei);
            }
            visited.get(cur).neighbors.push(visited.get(nei));
        } 
    }
    return visited.get(node);
};