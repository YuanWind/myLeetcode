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