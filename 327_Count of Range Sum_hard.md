# 327_Count of Range Sum_hard

## description

**Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.**

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

## example

```
Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
```

## analysis

先存储前缀和，然后遍历所有的[i][j]情况。
s[i][j]表示第i个到第j个数字的和。可以得出：
$$s(i,j)=s(0,j)-s(0,i-1)$$
因此先求出s(0,i),i=0···n的所有前缀和。

## python解法

```
def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    if not nums:
        return 0
    n=len(nums)
    ans=0
    dp=[]
    dp.append(nums[0])
    if lower<=dp[0]<=upper:
        ans+=1
    for i in range(1,n):
        dp.append(dp[i-1]+nums[i])
        if lower<=dp[i]<=upper:
            ans+=1
    for i in range(1,n):
        for j in range(1,i+1):
            if i==j and lower<=nums[j]<=upper:
                ans+=1
            elif lower<=dp[i]-dp[j-1]<=upper:
                ans+=1
    return ans
```

唉，最后超时了。
参考：用一个有序队列来记录前缀和的关系。$O(nlog(n))$
```
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        p = [0]                             #前缀和初始化，前缀和p[x]，就是区间数组[0, x)的和
        for i in nums:
            p += [p[-1] + i]                #前缀和计算
        ans = 0
        q = []                              #有序的前缀和队列
        for pi in p[:: -1]:                 #逆序遍历前缀和
            i, j = pi + lower, pi + upper   #给出当前前缀和两个对应边界
            l = bisect.bisect_left(q, i)    #二分查找
            r = bisect.bisect_right(q, j)   #找到对应边界的在前缀和数组里的插入位置   
            ans += r - l                    #序号大于自己的前缀和里有多少个前缀和在边界里面，就是以当前区间为起点，符合区间和条件的个数
            bisect.insort(q, pi)            #二分插入更新队列
        return ans
``` 