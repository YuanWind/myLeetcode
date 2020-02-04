# 112_Path Sum_easy

## description

**Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.**  

Each number in candidates may only be used once in the combination.

## example

Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

Example 2:
```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

## analysis

编号39题的升级版，回溯法，dfs搜索，需要判断相同解和添加访问数组确保每个元素只能被访问一次

## python解法

```
 def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    ans=[]
    candidates=sorted(candidates)
    visited=[1]*len(candidates)
    if target in candidates:
        ans.append([target])
    def dfs(target,index,path):
        path.sort()
        if target==0 and path not in ans:
            ans.append(path)
            return
        for i in range(index,len(candidates)):
            if target<candidates[i]:
                break
            if visited[i]!=0:
                visited[i]=0
                dfs(target-candidates[i],index,path+[candidates[i]])
                visited[i]=1
    dfs(target,0,[])
    return ans
```

打败了20.24%的人。

改进：
```
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    candidates.sort()#先排序，数组中相同的数字就会出现在一起
    n = len(candidates)
    def dfs(target, index, comb):
        if target == 0:
            return ans.append(comb)
        for i in range(index, n):
            if candidates[i] > target:
                break
            if i-1 >= index and candidates[i] == candidates[i-1]:
            #避免重复的搜索
                continue
            dfs(target - candidates[i], i+1, comb + [candidates[i]])
    dfs(target, 0, [])
    return ans
```