/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  if (nums.length < 3) {
    return [];
  }
  // Sort the input array nums
  const arr = nums.sort((a,b) => a-b);
  
  if (arr[0] > 0 || arr[arr.length - 1] < 0) {
    return [];
  }
    
  const n = arr.length;
  const res = [];
  for (let i = 0; i < n; i ++) {
    // If the current value is greater than zero, break from the loop
    if (nums[i] > 0) {
      return res;
    }
    // If the current value is the same as the one before, skip it
    if (i > 0 && arr[i] === arr[i - 1]) {
      continue;
    }
    // Otherwise two sum using two pointers for the current position i
    let l = i + 1;
    let r = n - 1;
    while(l < r) {
      const temp = arr[i] + arr[l] + arr[r];
      if (temp > 0) {
        r --;
      }
      if (temp < 0) {
        l ++;
      }
      if (temp === 0) {
        res.push([nums[i], nums[l], nums[r]]);
        // skip dup
        while(l < r && nums[l] === nums[l + 1]) {
          l ++;
        }
        while(l < r && nums[r] === nums[r - 1]) {
          r --;
        }
        l ++;
        r --;
      }
    }
  }
  return res;
};