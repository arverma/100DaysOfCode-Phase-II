#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                index = nums.index(target-nums[i], i+1)
                if index != i:
                    return [i, index]
            except:
                pass

# @lc code=end
