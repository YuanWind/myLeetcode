# 112_Path Sum_easy

## description

**Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.**  

## example

```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
```

## analysis

挺简单，遍历二叉树，每到叶子节点判断路径是否符合条件即可。

## python解法

```
def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    ans=[]
    def pre(node,target,path):
        if node==None:
            return
        if (node.left,node.right)==(None,None) and target==node.val:
            ans.append(path+[node.val])
            return
        pre(node.left,target-node.val,path+[node.val])
        pre(node.right,target-node.val,path+[node.val])
    pre(root,sum,[])
    return ans
```

60ms，打败了13.45%的人。
用dfs加上剪枝，要快一点，44ms
```
def pathSum(self, R: TreeNode, S: int) -> List[List[int]]:
    A, P = [], []
    def dfs(N):
        if N == None: return
        P.append(N.val)
        if (N.left,N.right) == (None,None) and sum(P) == S: A.append(list(P))
        else: dfs(N.left), dfs(N.right)
        P.pop()
    dfs(R)
    return A
```