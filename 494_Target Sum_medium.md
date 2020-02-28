# 494_Target Sum_medium

## description

**You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.**
**Find out how many ways to assign symbols to make sum of integers equal to target S.**  

## example

```
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```

## analysis

看到此题，首先想到了全排列树进行搜索,用dfs进行.可以结合剪枝条件

## python解法

```
def findTargetSumWays(self, nums: List[int], S: int) -> int:
    self.ans=0
    if not nums:
        if S!=0:
            return 0
        else:
            return 1
    def dfs(s,i):
        if s==S and i==len(nums):
            self.ans+=1
            return
        if i==len(nums):
            return
        if abs(s-S)>sum(nums[i:]): ##剪枝
            return
        dfs(s+nums[i],i+1)
        dfs(s-nums[i],i+1)
    dfs(0,0)
    return self.ans
```

可惜即使进行了剪枝还是超时了.

改用[动态规划解法](https://blog.csdn.net/mine_song/article/details/70216562?utm_source=copy).
```
def findTargetSumWays(self, nums: List[int], S: int) -> int:
    if sum(nums) < S or (sum(nums) + S) % 2 == 1: 
        return 0
    P = (sum(nums) + S) // 2
    dp = [1] + [0 for _ in range(P)]
    for num in nums:
        for j in range(P,num-1,-1):
            dp[j] = dp[j] + dp[j - num]
    return dp[P]
```