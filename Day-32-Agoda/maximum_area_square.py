class Solution:
    """
    https://leetcode.com/problems/maximal-square/
    """
    def maximalSquare(self, matrix) -> int:
        n = len(matrix)
        m = len(matrix[0])

        ans = 0
        matrix = [[0] + [int(ele) for ele in row] for row in matrix]
        matrix = [[0] * (m + 1)] + matrix
        for i in range(n + 1):
            for j in range(m + 1):
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                    ans = max(ans, matrix[i][j])
        return ans ** 2