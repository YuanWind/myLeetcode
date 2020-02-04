# 112_Path Sum_easy

## description

**Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.**  
**An example is the root-to-leaf path 1->2->3 which represents the number 123.**  
**Find the total sum of all root-to-leaf numbers.**  

## example

```
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

Example 2:
```
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

## analysis

挺简单，遍历一遍二叉树结果就出来了

## python解法

```
def sumNumbers(self, root: TreeNode) -> int:
    self.ans=0
    def pre(n,res):
        if n==None:
            return
        if (n.left,n.right)==(None,None):
            self.ans=self.ans+res*10+n.val
        pre(n.left,res*10+n.val)
        pre(n.right,res*10+n.val)
    
    pre(root,0)
    return self.ans
```