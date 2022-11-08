__author__ = 'aman.rv'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        visited = {}
        i = 0
        ans = 1
        for k, c in enumerate(s):
            if visited.get(c, -1) >= i:
                i = visited.get(c) + 1
            else:
                ans = max(k - i + 1, ans)
            visited[c] = k
        return ans

