// T.C. = O(logN) for how many times N(length of nums) can be indived by 2
// S.C. = O(1)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0;
    let r = nums.length - 1;
    
    while (l <= r) {
        let m = Math.floor(l + (r - l) / 2);
        if (nums[m] < target) {
            l = m + 1;
        } else if (nums[m] > target) {
            r = m - 1;
        } else {
            return m;
        }
    }
    
    return -1;
};