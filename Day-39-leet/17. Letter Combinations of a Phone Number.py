__author__ = 'aman.rv'


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        key = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = list(key[digits[0]])
        for d in digits[1::]:
            temp = []
            for c in key[d]:
                for a in ans:
                    temp.append(a + c)
            ans = temp
        return ans