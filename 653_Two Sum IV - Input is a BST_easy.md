# 112_Path Sum_easy

## description

**Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.**  

## example

### Example 1:

```
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True
 ```

 ```
Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
Output: False
```

## analysis

看到此题，遍历一遍二叉树，借鉴题目Two Sum做法。

## python解法

```
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.dic=set()
        self.ans=False
        def pre(root):
            if root!=None:
                res=k-root.val
                if res in self.dic:
                    self.ans=True
                    return
                else: 
                    self.dic.add(root.val)
                pre(root.right)
                pre(root.left)
        pre(root)
        return self.ans
```
如果初始化的dic为list，花费时间会大大增加。原因应该是list和set的底层实现原理不一样


