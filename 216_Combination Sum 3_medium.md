# 112_Path Sum_easy

## description

**Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.**  
```
Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.
```

## example

```
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
```

## analysis

挺简单，一遍过，dfs一下。

## python解法

```
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    ans=[]
    def dfs(target,index,path):
        if target==0 and len(path)==k:
            ans.append(path)
            return
        for i in range(index,10):
            dfs(target-i,i+1,path+[i])
    dfs(n,1,[])
    return ans
```