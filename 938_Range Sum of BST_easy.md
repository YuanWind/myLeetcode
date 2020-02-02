# 938_Range Sum of BST_easy

## description

**Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).**  

## example

### Example 1:

```
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
```

```
Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
```

## analysis

遍历二叉树即可得到结果

## python解法

```
def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    self.ans=0
    def pre(root):
        if root!=None:
            if L<=root.val<=R :
                self.ans+=root.val
            pre(root.left)
            pre(root.right)
    pre(root)
    return self.ans
```
提交后答案正确了，但是花费的时间去很长，排名很低。分析原因，BST为二叉搜索树，左子树一定小于当前节点的值，右子树大于当前节点的值，所以可以利用该条件进行剪枝。
```
def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    self.ans=0
    def pre(root):
        if root!=None:
            if L<=root.val<=R :
                self.ans+=root.val
            if L<root.val:
                pre(root.left)
            if R>root.val:
                pre(root.right)
    pre(root)
    return self.ans
```