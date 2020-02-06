# 112_Path Sum_easy

## description

**Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).**  
||||||
|-|-|-|-|-|
|3|0|1|4|2|
|5|6|3|2|1|
|1|2|0|1|5|
|4|1|0|1|7|
|1|0|3|0|5|
|||||
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.


## example

```
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
```

## analysis

简单的方法可以直接暴力解题。
此题利用动态规划解题。详细[解题思路](https://leetcode.com/articles/range-sum-query-2d-immutable/)

## python解法

```
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix==None or matrix==[]:
            return
        self.m,self.n=len(matrix),len(matrix[0])
        self.dp=[[0]*(self.n+1) for _ in range(self.m+1)]
        self.dp[0][0]=matrix[0][0]
        for i in range(1,self.m):
            self.dp[i][0]=self.dp[i-1][0]+matrix[i][0]
        for i in range(1,self.n):
            self.dp[0][i]=self.dp[0][i-1]+matrix[0][i]
        for i in range(1,self.m):
            for j in range(1,self.n):
                self.dp[i][j]=self.dp[i-1][j]+self.dp[i][j-1]-self.dp[i-1][j-1]+matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        A=self.dp[row1-1][col1-1]
        B=self.dp[row2][col1-1]
        C=self.dp[row1-1][col2]
        D=self.dp[row2][col2]
        return A+D-B-C


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```