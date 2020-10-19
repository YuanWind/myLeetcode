# 867_Transpose Matrix_easy

## description

**Given a matrix A, return the transpose of A.**

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

## example

```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

## analysis

循环一下，B[i]\[j\]=A[j][i\]

## python解法

```python
#法一：
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(A)
        n=len(A[0])
        B=[[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                B[i][j]=A[j][i]
        return B
#法二：
class Solution(object):
    def transpose(self, A):
         return [list(i) for i in zip(*A)]
```

法二巧用了zip函数，更为简洁。