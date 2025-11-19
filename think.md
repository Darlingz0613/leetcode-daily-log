# **11.18**
NO.1 
717. 1 比特与 2 比特字符
简单

有两种特殊字符：

    第一种字符可以用一比特 0 表示
    第二种字符可以用两比特（10 或 11）表示

给你一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一个一比特字符，则返回 true 。

示例 1:

输入: bits = [1, 0, 0]
输出: true
解释: 唯一的解码方式是将其解析为一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。


思路：
1.数一数一的个数,如果1的格式是奇数那就是错  X
先分情况 
    全是1       11 11 就这一种可能 最后一个字符必定不是0
    结尾一个0    11 10 不是
                11 0
    中间有0     10 10 11 10 0        1是奇数 0是偶数
                10 11 10 0 10 11

                10 11 10 0
            如果最后一个是 1 一定错
看题解...
    从前往后看   如果是0的话就无所谓
                如果是1的话下一位必须绑定
                if 0 去掉
                if 1 去掉这一位和下一位
代码：
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        n=len(bits)
        while i<n-1:
            if bits[i]==0:
                i+=1
            else:
                i+=2
        return i==n-1

NO.2
Q1. 错误的集合
简单
相关标签
premium lock icon相关企业

集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]

思路：
    我可以找一个i直接遍历从1到n找出缺失
问了句kimi
*把“原集合 1‥n 的总和”与“当前数组的总和、总个数”各算一次，重复数字由总和差推出，缺失数字由重复数字和总和差联合推出——只用两次累加，无需额外空间。*

 n = len(nums)
        S = sum(nums)                    # 数组总和
        T = n * (n + 1) // 2             # 1..n 正确总和
        seen = set()
        for v in nums:                   # 遍历的是“值”，不是下标
            if v in seen:
                dup = v                  # 抓到重复数
                break
            seen.add(v)
        missing = dup - (S - T)          # 由总和差算出缺失数
        return [dup, missing]


eg ：
---
id: 001
title: 两数之和
tags: [数组, 哈希表]
difficulty: Easy
date: 2025-11-18
---

## 1. 题干 & 链接
- 题目描述：…（复制官方题干或贴截图）
- 链接：https://leetcode.cn/problems/two-sum/

## 2. 思路快照
- 10 秒思路：暴力枚举 → O(n²)
- 优化方向：用哈希表存已经看过的数 → O(n)

## 3. 详细推演
1. 画图/举例：nums = [2,7,11,15], target = 9  
   手绘草图：![手绘草图](assets/001_sketch.jpg)
2. 伪代码：
   ```text
   map = {}
   for i, x in enumerate(nums):
       if target-x in map:
           return [map[target-x], i]
       map[x] = i



---
id: 2154
title: 
tags: [数组, 哈希表]
difficulty: Easy
date: 2025-11-18
---

## 1. 题干 & 链接
- 题目描述：给你一个整数数组 nums ，另给你一个整数 original ，这是需要在 nums 中搜索的第一个数字。

接下来，你需要按下述步骤操作：

如果在 nums 中找到 original ，将 original 乘以 2 ，得到新 original（即，令 original = 2 * original）。
否则，停止这一过程。
只要能在数组中找到新 original ，就对新 original 继续 重复 这一过程。
返回 original 的 最终 值。
- 链接：https://leetcode.cn/problems/two-sum/

## 2. 思路快照
- 直接贪心就ok

## 3. 详细推演
1. 画图/举例：nums = [2,7,11,15], target = 9  
   手绘草图：![手绘草图](assets/001_sketch.jpg)
2. 伪代码：
   ```text
   class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        m=max(nums)
        n=len(nums)
        while original<=m:
            if original in nums:
                original=original*2
            else:
                break
        return original


---
id: 1365
title: 
tags: [数组, 哈希表]
difficulty: Easy
date: 2025-11-18
---

## 1. 题干 & 链接
- 题目描述：给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

以数组形式返回答案。
- 链接：https://leetcode.cn/problems/two-sum/

## 2. 思路快照
- 10 秒思路：暴力枚举 → O(n²)
- 优化方向：用哈希表存已经看过的数 → O(n)

## 3. 详细推演
1. 画图/举例：nums = [2,7,11,15], target = 9  
   手绘草图：![手绘草图](assets/001_sketch.jpg)
2. 伪代码：
   ```class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        for i in nums:
            cnt=0
            for j in nums:
                if i>j:
                    cnt+=1
            a.append(cnt)
        return a


---
id: 448
title: 
tags: [数组, 哈希表]
difficulty: Easy
date: 2025-11-18
---

## 1. 题干 & 链接
- 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。。

以数组形式返回答案。
- 链接：https://leetcode.cn/problems/two-sum/

## 2. 思路快照
- 10 秒思路：暴力枚举 → O(n²)
- 优化方向：用哈希表存已经看过的数 → O(n)

## 3. 详细推演
1. 画图/举例：nums = [2,7,11,15], target = 9  
   手绘草图：![手绘草图](assets/001_sketch.jpg)
2. 伪代码：
   ```class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen=set(nums)
        a=[]
        for i in range(1,n+1):
            if i not in seen:
                a.append(i)
        return a