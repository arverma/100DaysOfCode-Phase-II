#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z")
        }

        if digits == "":
            return[]
        temp = []
        res = keypad.get(digits[0], [])
        for d in digits[1::]:
            for r in res:
                for l in keypad.get(d):
                    temp.append(r + l)
            res = temp[:]
            temp = []
        return res

# @lc code=end
