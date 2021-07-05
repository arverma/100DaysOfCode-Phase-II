#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
import math


class Solution:
    def romanToInt(self, string: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        res = 0
        past = ""
        for s in string:
            if roman.get(past, math.inf) < roman[s]:
                res += (roman[s] - 2*roman[past])
            else:
                res += roman[s]
            past = s
        return res
# @lc code=end
