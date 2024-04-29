

# Method 1: This is recursive Memoization solution

class Solution(object):
    def minFallingPathSum(self, matrix):
        N = len(matrix)
        ans = 100000
        cache = {}
        for c in range(N):
            # Traverse from all the cells in the first row
            ans = min(self.dfs(0, c, matrix, cache), ans)
        return ans

    def dfs(self, r, c, matrix, cache):
        N = len(matrix)
        if r == N:
            return 0
        if c < 0 or c == N:
            return float("inf")
        if (r, c) in cache:
            return cache[(r, c)]
        # Check if you would find the minimum path by travelling diagonal left, below and diagonal right
        res = matrix[r][c] + min(self.dfs(r + 1, c - 1, matrix, cache), self.dfs(r + 1, c, matrix, cache),
                                 self.dfs(r + 1, c + 1, matrix, cache))
        cache[(r, c)] = res
        return res


# Method 2:
# The below code is bottom up approach using dynamic programming
    def minFallingPathSum(self, matrix):
        N = len(matrix)
        for r in range(1, N):
            for c in range(N):
                up = matrix[r - 1][c]
                left = matrix[r - 1][c - 1] if c > 0 else float("inf")
                right = matrix[r - 1][c + 1] if c < N - 1 else float("inf")
                matrix[r][c] += min(up, left, right)
        return min(matrix[-1])

