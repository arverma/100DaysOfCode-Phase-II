__author__ = 'aman.rv'


class Solution:
    def reverse(self, x: int) -> int:
        y = int(str(abs(x))[::-1])
        res = y if x >= 0 else -y
        return res if -2 ** 31 < res < 2 ** 31 else 0
