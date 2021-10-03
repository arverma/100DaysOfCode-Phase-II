#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Solution 1( DEcrement method)
        return sum(nums) - len(nums)*min(nums)

# @lc code=end
