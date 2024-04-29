
#Method 1: This is bottom up approach using Dynamic Programming
def minFallingPathSum(self, grid):
    N = len(grid)
    for r in range(1, N):
        for c in range(N):
            ans = 999999999
            j = 0
            while (j < c):
                element = grid[r - 1][j]
                ans = min(ans, grid[r][c] + element)
                j = j + 1
            j = c + 1
            while (j <= N - 1):
                element = grid[r - 1][j]
                ans = min(ans, grid[r][c] + element)
                j = j + 1
            grid[r][c] = ans
    return min(grid[-1])

#Method 2: Recusive approach using Memoization
def minFallingPathSum(self, grid):
    N = len(grid)
    ans = 99999999
    cache = {}
    for i in range(N):
        ans = min(self.dfs(0, i, N, cache, grid), ans)
    return ans

def dfs(self, r, c, N, cache, grid):
    if r == N - 1:
        return grid[r][c]
    # Out of bounds checks
    if c < 0 or c >= N:
        return float('inf')
    # Check the cache
    if (r, c) in cache:
        return cache[(r, c)]

    ans = float('inf')  # Reset ans for each call
    # Explore all columns in the next row except the same column c.
    for i in range(N):
        if i != c:
            ans = min(ans, self.dfs(r + 1, i, N, cache, grid))

    # Accumulate the sum for the current path
    res = grid[r][c] + ans
    # Cache the result before returning
    cache[(r, c)] = res
    return res


#Method 3: Most Optimized Solution just by picking the min two elements from every row
def minFallingPathSum(self, grid):
    N = len(grid)
    first_row = [(val, ind) for ind, val in enumerate(grid[0])]
    dp = self.get_two_smallest(first_row)
    for r in range(1, N):
        next_dp = []
        for curr_c in range(N):
            ans = 999999
            for prev_val, prev_c in dp:
                if prev_c != curr_c:
                    ans = min(ans, grid[r][curr_c] + prev_val)
            next_dp.append((ans, curr_c))
            next_dp = self.get_two_smallest(next_dp)
        dp = next_dp
    return min([val for val, ind in dp])

def get_two_smallest(self, row):
    two_smallest = []
    for val, ind in row:
        if len(two_smallest) < 2:
            two_smallest.append((val, ind))
        elif two_smallest[1][0] > val:
            two_smallest.pop()
            two_smallest.append((val, ind))
        two_smallest.sort()
    return two_smallest

#Link: https://leetcode.com/problems/minimum-falling-path-sum-ii/?envType=daily-question&envId=2024-04-26
#Solution Video: https://www.youtube.com/watch?v=_b8sptrsFEM&t=1646s
