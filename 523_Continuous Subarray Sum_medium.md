# 112_Path Sum_easy

## description

**Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.**  

## example

```
Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
```

## analysis

利用前缀和解题. 前缀和数组sum[j]表示下标为j以前的所有数字和. 故问题实际是求(sum[j]-sum[i])%k==0? (sum[j]-sum[i])%k=sum[j]%k-sum[i]%k==0? 表示(i,j]左开又闭之间的sum, 故有sum[j]%k=sum[i]%k, 所以当有第二次求到同一个余数时, 并且i,j之间的距离>1时才符合要求. 为了快速求一个余数是不是第二次出现, 所以先用一个map保存已经出现的余数, 求出一个余数时可以判断在map中的键是否出现过. 同时可以把下标i,j 等下标信息保存到map的值中用来判断二者之间的下标距离是否大于1. 同时我们要初始化一个{0:-1}来表示前两个数字就返回True的情况.

## python解法

```
def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    sum_val = 0
    res = {}
    res[0] = -1
    for idx,num in enumerate(nums):
        sum_val += num
        if k != 0:
            sum_val = sum_val%k
        if sum_val in res.keys():
            if idx - res[sum_val] > 1:
                return True
        else:
            res[sum_val] = idx
    return False
```