# 112_Path Sum_easy

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

看到此题，首先就想到了dfs搜索。

## python解法

```
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if root==None:
        return
    if (root.left,root.right)==(None,None):
        return root.val==sum
    return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
```