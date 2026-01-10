/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    const idx = nums.indexOf(target - nums[i]);
    if (idx !== -1 && idx !== i) return [i, idx];
  }
};
