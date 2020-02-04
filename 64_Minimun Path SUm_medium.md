# 64_Minimum Path Sum_medium

## description

**Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.**  

## example

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

## analysis

首先就想到了使用bfs，因为有限制条件Minimum，即最优解。

## python解法

```
def minPathSum(self, grid: List[List[int]]) -> int:
    self.ans=float('inf')
    n=len(grid)
    m=len(grid[0])
    def dfs(i,j,res):
        if self.ans<res:return
        if i==n-1 and j==m-1 and self.ans>res+grid[i][j]:
            self.ans=res+grid[i][j]
            return
        if i+1<n and j<m:
            dfs(i+1,j,res+grid[i][j])
        if i<n and j+1<m:
            dfs(i,j+1,res+grid[i][j])
    dfs(0,0,0)
    return self.ans
```

可惜了，结果应该都没问题，但是最后评测结果超时了。参考了讨论区的解法后，发现要用动态规划。  
使用动态规划解题，将待求解问题分解成若干子问题，先求解子问题，再结合这些子问题的解得到原问题的解。  
待求解问题：从[0][0]到[m][n]的最短距离，使dp[i][j]表示从[0][0]到[i][j]的最优解。可以有：
$$dp(i,j)= \begin{cases}
grid(0,0) & i,j=0\\
dp(i-1,0)+grid(i,0) & i>0,j=0\\
dp(0,j-1)+grid(0,j) & i=0,j>0\\
min(dp(i-1,j),dp(i,j-1))+grid(i,j) & i,j>=1
\end{cases}$$
```
def minPathSum(self, grid: List[List[int]]) -> int:
    m,n=len(grid),len(grid[0])
    dp=[[0]*n for _ in range(m)]
    dp[0][0]=grid[0][0]
    for i in range(1,m):
        dp[i][0]=dp[i-1][0]+grid[i][0]
    for i in range(1,n):
        dp[0][i]=dp[0][i-1]+grid[0][i]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=min(dp[i][j-1],dp[i-1][j])+grid[i][j]
    return dp[m-1][n-1]
```

