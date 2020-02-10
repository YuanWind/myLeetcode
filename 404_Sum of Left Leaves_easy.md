# 404_Sum of Left Leaves_easy

## description

**Find the sum of all left leaves in a given binary tree.**  

## example

```
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
```

## analysis

遍历一遍二叉树即可。

## python解法

```
class Solution:
    def pre(self,root):
        if not root:return
        if root.left !=None and (root.left.left,root.left.right)==(None,None):
            self.ans+=root.left.val
        if root.left!=None:self.pre(root.left)
        if root.right!=None:self.pre(root.right)
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:return 0
        self.ans=0
        self.pre(root)
        return self.ans
```