# 410_Split Array Largest Sum_hard

## description

**Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.**  

## example

```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

## analysis

先想到的是动态规划来解，奈何找不到最优子结构。看题解，有[二分查找解题](https://leetcode-cn.com/problems/split-array-largest-sum/solution/pao-ding-jie-niu-dai-ni-yi-bu-bu-shi-yong-er-fen-c/)，还有[动态规划解题](https://leetcode-cn.com/problems/split-array-largest-sum/solution/pythondong-tai-gui-hua-er-fen-fa-by-idealworld/)

## python解法

### 二分查找
```
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
    def group(mid):
        sums=0
        cnt=1
        for i in nums:
            if sums + i > mid:
                cnt += 1
                sums = i
            else:
                sums += i
        return cnt

    left, right = max(nums),sum(nums)
    while left < right:
        mid = (left + right) // 2
        if group(mid) <= m:
            right = mid
        else:
            left = mid + 1
    return left
```

### 动态规划

```
def splitArray(self, nums: List[int], m: int) -> int:
        presum = [0 for i in range(len(nums))]
        presum[0] = nums[0]
        for i in range(1, len(nums)):
            presum[i] =  presum[i-1]  + nums[i]
        # presum[j] - presum[i] = [i+1, j]
        # f[i][j]表示从nums[0]~nums[j]分成i组的解
        f = [[float('inf')] * len(nums) for i in range(m+1)]
        # f[1][j] = sum(0, j), 包含边界，表示只划分一段时的解
        for j in range(len(nums)):
            f[1][j] = presum[j]
        for i in range(2, m + 1):
            for j in range(i - 1, len(nums)):
                for k in range(0, j):
                    f[i][j] = min(f[i][j], max(f[i-1][k], presum[j] - presum[k]))
        return f[m][len(nums)-1]
```