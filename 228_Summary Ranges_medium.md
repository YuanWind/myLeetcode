# 228_Summary Ranges_medium

## description

**Given a sorted integer array without duplicates, return the summary of its ranges.**  

## example

Example 1:
```
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
```

Example 2:
```
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
```

## analysis

一开始老被边界条件麻烦，各种if，尤其是要判断最后一个数字与前边数字的关系的时候。后来灵感突现，我在原来的数组最后加个数字，让原来的最后一个不是最后一个数字就好了。最后只用了两次判断就ok啦

## python解法

```
def summaryRanges(self, nums: List[int]) -> List[str]:
    if nums==[]:
        return []
    n=len(nums)
    ans=[]
    nums.append(nums[-1]+2)
    res=str(nums[0])
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]>1 and i-1>0 and nums[i-1]-nums[i-2]==1:
            res=res+"->"+str(nums[i-1])
            ans.append(res)
            res=str(nums[i])
        elif nums[i]-nums[i-1]>1:
            ans.append(res)
            res=str(nums[i])
    return ans
```
打败了86.25% 的提交。还不错