
# 39_Combination Sum_mediun

## description

**Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.**

The same repeated number may be chosen from candidates unlimited number of times.  

## example

Example 1:
```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

Example 2:
```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

## analysis

看到此题，应该联想到回溯法来解题。画出解空间树，应该为子集树，用dfs搜索

## python解法

```
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    new_candidates=[i for i in candidates if i<=target]
    self.ans=[]
    res=[]
    if new_candidates==[]:
        return self.ans
    minximal=min(new_candidates)
    def dfs(candidates,target,res,minximal):
        res.sort()
        if target==0 and res not in self.ans:
            self.ans.append(res)
            return

        for i in candidates:
            if target>=minximal:
                res.append(i)
                dfs(candidates,target-i,copy.copy(res),minximal)
                res.pop()
    dfs(new_candidates,target,res,minximal)
    return self.ans
```
运行时间打败了5%的人。看了下排名靠前的。可以看出，上边的做法会产生许多重复的结果(例如[2,3,2],[2,2,3])，所以进行了判断。以下进行了剪枝改进，未产生重复的结果，花费时间减少。

改进：
```
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates = sorted(candidates)
    res = []
    def dfs(target, index, path):
        if target == 0:
            res.append(path)
            return
        
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            dfs(target-candidates[i], i, path + [candidates[i]])
    
    dfs(target, 0, [])
    return res
```