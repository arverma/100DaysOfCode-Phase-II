#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, string: str, p: str) -> bool:
        n = len(string)
        m = len(p)
        res = [[False for i in range(m+1)] for j in range(n+1)]
        res[0][0] = True

        for i in range(2, m+1):
            if p[i-1] == "*":
                res[0][i] = res[0][i-2]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1] in (string[i-1], "."):
                    res[i][j] = res[i-1][j-1]
                elif p[j-1] == "*":
                    res[i][j] = res[i][j-2]
                    if p[j-2] in (string[i-1], "."):
                        res[i][j] = res[i][j] or res[i-1][j]
                else:
                    res[i][j] = False
        return res[n][m]

# @lc code=end
