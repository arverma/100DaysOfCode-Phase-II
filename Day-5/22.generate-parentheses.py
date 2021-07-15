#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.balanced_parenthesis("", n, 0, 0, [])

    def balanced_parenthesis(self, s, n, o, c, res):
        if len(s) == 2*n:
            res.append(s)
        else:
            if o > c:
                self.balanced_parenthesis(s + ")", n, o, c + 1, res)
            if o < n:
                self.balanced_parenthesis(s + "(", n, o + 1, c, res)
        return res

# @lc code=end
