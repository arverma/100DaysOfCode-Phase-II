#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        flag = ""
        if len(s) <= 1:
            return 0 if s.isdigit() == False else int(s)
        if s[0] in ("-", "+"):
            flag = s[0]
            s = s[1::]
        if s.isdigit():
            return min(max((-2)**31, int(flag+s)), (2)**31-1)
        elif (s[0].isdigit() and "".join(s.split())) or (s[0].isdigit() and s.split(".")[0].isdigit()):
            try:
                res = s.split(".")[0]
                int(res)
            except:
                res = ""
                for i in s:
                    if i.isdigit():
                        res += i
                    else:
                        break
            return min(max((-2)**31, int(flag+res)), (2)**31-1)
        else:
            return 0

# @lc code=end
