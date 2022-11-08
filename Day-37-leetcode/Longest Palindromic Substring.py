__author__ = 'aman.rv'


class Solution:
    def find_palindrome_length(self, s, n, ans, l, r):
        while l > -1 and r < n and s[l] == s[r]:
            if r - l + 1 > ans[1] - ans[0]:
                ans = [l, r]
            l -= 1
            r += 1
        return ans

    def longestPalindrome(self, s: str) -> str:
        ans = [0, 0]
        for i in range(len(s)):
            ans = self.find_palindrome_length(s, len(s), ans, i, i)
            ans = self.find_palindrome_length(s, len(s), ans, i, i + 1)

        return s[ans[0]:ans[1] + 1]