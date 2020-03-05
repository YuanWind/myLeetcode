# 112_Path Sum_easy

## description

**Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.**  

## example

```
Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
```

## analysis

思考了一下, 想到的是暴力, 但是搜索到哪个数字结束呢? 初步想的是既然两个数各自平方和=c, 那么搜索时最大肯定是$0^2+n^2=c$中的n. 故n=$\sqrt{c}$, 注意的是需要单独判断两种情况:1.c本来就可以开平方得整数 2.c/2可以开平方得整数. 

## python解法

```
def judgeSquareSum(self, c: int) -> bool:
    n=c**0.5
    if int(n)==n:
        return True
    else:
        n=int(n)
    dic={}
    for i in range(1,n+1):
        j=i*i
        if j+j==c:
            return True
        if (j) not in dic:
            dic[c-j]=1
        else:
            return True
    return False
```
后来参考题解, 有其它两种更好的方法

1. 直接费马定理:
    - 引理1：形如4k+3的自然数不能表示成2个整数的平方和
    - 引理2：正整数n可被表示为两整数平方和的充要条件为n的一切形如4k+3形状的质因子的幂次均为偶数

```
def judgeSquareSum(self, c: int) -> bool:
    for i in range(2,int(math.sqrt(c))+1):
        count=0
        while c%i==0:
            count+=1
            c/=i
        if i%4==3 and count%2==1:
            return False
    return c%4!=3
```

2. 二分法(利用双指针)

```
def judgeSquareSum(self, c: int) -> bool:
    idx2 = int(math.sqrt(c))
    idx1 = 0
    numbers = [i+1 for i in range(idx2)]
    while(idx1 <= idx2):
        twosum = idx1 ** 2 + idx2 ** 2
        if (twosum == c):
            return True
        elif (twosum < c):
            idx1 += 1
        else :
            idx2 -= 1
    return False
```