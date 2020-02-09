# 377_Combination Sum IV_medium

## description

**Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.**  

## example

```
Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
```

## analysis

本来想的是dfs搜索，最后超时了。看[题解](https://leetcode-cn.com/problems/combination-sum-iv/solution/dong-tai-gui-hua-python-dai-ma-by-liweiwei1419/)

## python解法

```
def combinationSum4(self, nums: List[int], target: int) -> int:
    if not nums:
        return 0
    dp=[0 for _ in range(target+1)]
    dp[0]=1
    for i in range(1,target+1):
        for j in range(len(nums)):
            if i >=nums[j]:
                dp[i]+=dp[i-nums[j]]
    return dp[-1]
```