# 1_Two Sum_easy

## description

**Given an array of integers, return indices of the two numbers such thar they add up to a specific target.**  
You may assume that each input would have exactly one solution, and you may not use the same element twice.

## example

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## analysis

1. 暴力解法：很容易想到，两重循环，注意不要选择下标相同的两个数就行了。时间复杂度$O(n^2)$

2. 用hash表解决，将数组中每个数字作为hash表的key，下标作为hash表的value（因为最后要求输出索引值）。如果target-nums[i]在hash表中的key中存在，就说明nums[i]和hash[target-nums[i]]的和为target。输出即可。

## python解法

### 1. 暴力破解

```
def twoSum(self, nums: List[int], target: int) -> List[int]:
    i=0
    j=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i]+nums[j]==target:
                return [i,j]
    return []
```

结果运行超时！由于python本身效率不如c++，所有c++可以通过但是python无法通过

### 2. two-pass hash table

```
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic={value:index for index,value in enumerate(nums)}
    for i in range(len(nums)):
        value=target-nums[i]
        index=dic.get(value)
        if index and index!=i:
            return [i,index]
    return []
```

结果accept，这里还用了两次单重循环，可以优化，边添加边判断。

### 3. one-pass hash table

```
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic={}
    for idx,num in enumerate(nums):
        res=target-num
        if res in dic:
            return [idx,dic[res]]
        dic[num]=idx
```

类似题目链接：[leetcode题集中搜索sum](https://leetcode.com/problemset/all/?search=sum)