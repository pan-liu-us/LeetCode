/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    let in_degree_list = new Array(numCourses).fill(0);
    let adj_list = new Array(numCourses).fill(0).map(() => []);
    
    for (let [course, preCourse] of prerequisites) {
        in_degree_list[course]++;
        adj_list[preCourse].push(course);
    }
    
    // find nodes with 0 in-degree and push them to queue
    let queue = [];
    for (let i = 0; i < in_degree_list.length; i++) {
        if (in_degree_list[i] === 0) {
              queue.push(i);          
        }
    }
    
    let res = []

    // traverse nodes in topological order until queue is empty
    while (queue.length) {
        let current = queue.shift();
        res.push(current);
        numCourses--;
        for (let v of adj_list[current]) {
            in_degree_list[v]--;
            if (in_degree_list[v] === 0) {
                queue.push(v);
            }
        }
    }
    
    if (numCourses === 0) {
        return res;
    } else {
        return [];
    }
};