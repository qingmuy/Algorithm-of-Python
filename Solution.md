# 题目以及解析

LeetCode：100x

卡码：300x

 

## 目录

### 数据结构

#### 字符串

[1003 - 罗马数字转整数](#p1003)

[1004 - 最长公共前缀](#p1004)

[1005 - 有效的括号](#p1005)

[1009 - 找出字符串中第一个匹配项的下标](#p1009)

[1011 - 最后一个单词的长度](#p1011)

[1013 - 二进制求和](#p1013)

[1029 - 验证回文串](#p1029)

[1036 - 反转字符串](#p1036)

[1037 - 反转字符串 II](<a id="p1037"></a>)

[1039 - 密钥格式化](#p1039)

[1049 - 有效的字母异位](#p1049)

[1053 - 赎金信](#p1053)

[1056 - 反转字符串中的单词](#p1056)

[1057 - 重复的子字符串](#p1057)

[3001 - 替换数字](#p3001)

[3002 -  右旋字符串](#p3002)

[1058 - 删除字符串中的所有相邻重复项](#p1058)



#### 链表

[1006 - 合并两个有序链表](#p1006)

[1016 - 删除排序链表中的重复元素](#p1016)

[1031 - 环形链表](#p1031)

[1043 - 设计链表](#p1043)

[1044 - 反转链表](#p1044)

[1046 - 删除链表的倒数第N个结点](#p1046)

[1047 - 链表相交](#p1047)



#### 栈

[1005 - 有效的括号](#p1005)

[1018：二叉树的中序遍历](#p1018)

[1058 - 删除字符串中的所有相邻重复项](#p1058)

[1059 - 逆波兰表达式求值](#p1059)



#### 队列

[1060 - 滑动窗口的最大值](#p1060)



#### 树

[1018 - 二叉树的中序遍历](#p1018)

[1019 - 相同的树](#p1019)

[1020 - 对称二叉树](#p1020)

[1021 - 二叉树的最大深度](#p1021)

[1022 - 将有序数组转换为二叉搜索树](#p1022)

[1023 - 平衡二叉树](#p1023)

[1024 - 二叉树的最小深度](#p1024)

[1025 - 路径总和](#p1025)

[1032 - 二叉树的前序遍历](#p1032)

[1033 - 二叉树的后序遍历](#p1033)



#### 哈希表

[1001 - 两数之和](#p1001)

[1003 - 罗马数字转整数](#p1003)

[1049 - 有效的字母异位](#p1049)

[1050 - 两个数组的交集](#p1050)

[1051 - 快乐数](#p1051)

[1052 - 四数相加 II](#p1052)

[1053 - 赎金信](#p1053)

[1061 - 前k个高频元素](#p1061)



### 解题方法

#### 双指针

[1007 - 删除有序数组中的重复项](#p1007)

[1008 - 移除元素](#p1008)

[1009 - 找出字符串中第一个匹配项的下标](#p1009)

[1017 - 合并两个有序数组](#p1017)

[1029 - 验证回文串](#p1029)

[1031 - 环形链表](#p1031)

[1036 - 反转字符串](#p1036)

[1038 - 有序数组的平方](#p1038)

[1046 - 删除链表的倒数第N个结点](#p1046)

[1047 - 链表相交](#p1047)

[1054 - 三数之和](#p1054)

[1055 - 四数之和](#p1055)

[1056 - 反转字符串中的单词](#p1056)



#### 动态规划

[1015 - 爬楼梯](#p1015)

[1026 - 杨辉三角](#p1015)

[1027 - 杨辉三角 II](#p1027)

[1028 - 买卖股票的最佳时机](#1028)



#### 递归

[1006 - 合并两个有序链表](#p1006)

[1018 - 二叉树的中序遍历](#p1018)

[1032 - 二叉树的前序遍历](#p1032)

[1033 - 二叉树的后序遍历](#p1033)



#### 二分查找

[1010 - 搜索插入位置](#p1010)

[1014 - x的平方根](#p1014)

[1035 - 二分查找](#p1035)

[1040 - 长度最小的子数组](#p1040)



#### 位运算

[1013 - 二进制求和](#p1013)

[1030：只出现一次的数字](#p1030)



#### 滑动窗口

[1040 - 长度最小的子数组](#p1040)

[1060 - 滑动窗口的最大值]()



#### 前缀和

[1040 - 长度最小的子数组](#p1040)



#### 模拟

[1041 - 螺旋矩阵 II](#p1041)



## 题目列表

### 1001 - 两数之和<a id="p1001"></a>

#### 题目

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** *`target`* 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。



**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```



#### 解法

暴力解法

```python
# 双层遍历
# 内部设置判断条件if

from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if nums[i] + nums[j] == target and i != j:
                    return[i,j]
        return[]
    

'''
    列表中的值是可以重复的，去重方法：转为set集合
    对于列表有默认方法len方法：可以获取指定列表的索引长度，获取的值即为列表的元素个数 - 1
    同时存在index方法：获取某个元素在列表中的索引（可指定范围，默认获取第一个相同的值的索引）
'''
```

字典法

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = {}
        for index, num in enumerate(nums):
            if (target - num) in records:
                return [index, records[target - num]]
            else:
                records[num] = index
```





### 1002 - 回文数<a id="p1002"></a>

#### 题目

给你一个整数 `x` ，如果 `x` 是一个回文整数，返回 `true` ；否则，返回 `false` 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

- 例如，`121` 是回文，而 `123` 不是。

 

**示例 1：**

```
输入：x = 121
输出：true
```

**示例 2：**

```
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```

**示例 3：**

```
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
```



#### 解法

```python
'''
    转换为字符串，比较字符串即可
    问题：内存较大
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) != reversed(str(x)):
            return False
        else:
            return True
```



### 1003 - 罗马数字转整数<a id="p1003"></a>

#### 题目

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 `2` 写做 `II` ，即为两个并列的 1 。`12` 写做 `XII` ，即为 `X` + `II` 。 `27` 写做 `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 
- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。

 

**示例 1:**

```
输入: s = "III"
输出: 3
```

**示例 2:**

```
输入: s = "IV"
输出: 4
```

**示例 3:**

```
输入: s = "IX"
输出: 9
```

**示例 4:**

```
输入: s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
```

**示例 5:**

```
输入: s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```



#### 解法

```python
'''
    切割字符串
    设置字典
    遍历相加

    问题：如何切割？
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        sum = 0
        for i,n in enumerate(s):
        sum += d.get(s[max(i-1, 0):i+1],d[n])
        return sum  

    思想：遍历，对于4、9之类的特殊字符，每次读取两位，如果不能寻找就加当前位
    对于开头存在特殊字符的处理：将特殊字符在字典内的值-1即可，实现对于重复加的处理
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
```



### 1004 - 最长公共前缀<a id="p1004"></a>

#### 问题

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

 

**示例 1：**

```
输入：strs = ["flower","flow","flight"]
输出："fl"
```

**示例 2：**

```
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
```



#### 解法

```python
'''
    对字符串进行遍历
    每次从首字母截取，拓展，一旦不匹配则返回值
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char = ([strs[i] for i in range(len(strs))])

        for x in range(1,len(max(strs,key = len))):
            i = set([str[:x] for str in char])
            if len(i) > 1 and x == 1:
                return ''
            elif len(i) > 1:
                return char[1][:x - 1]
```



### 1005 - 有效的括号<a id="p1005"></a>

#### 问题

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

 

**示例 1：**

```
输入：s = "()"
输出：true
```

**示例 2：**

```
输入：s = "()[]{}"
输出：true
```

**示例 3：**

```
输入：s = "(]"
输出：false
```



#### 解法

列表天生就是栈，运用栈的思维解决问题

```python
'''
    转为列表
    使用字典 or 列表
    (,[,{,},],)
    回文数问题判断，不符False
'''
class Solution:
    def isValid(self, s: str) -> bool:
        # 简单逻辑判断，如果字符串个数并非偶数则直接不闭合
        if len(s) % 2 != 0:
            print("字符串长度不符合")
            return False
        
        # 创建列表记录括号数目，转为字符串判断回文数，若非回文数直接False
        Valid = [0,0,0,0,0,0]
        for i in s:
            if i == "(":
                Valid[0] += 1
            elif i == "[":
                Valid[1] += 1
            elif i == "{":
                Valid[2] += 1
            elif i == "}":
                Valid[3] += 1
            elif i == "]":
                Valid[4] += 1
            elif i == ")":
                Valid[5] += 1
        if ''.join([str(i) for i in Valid]) != ''.join([str(i) for i in Valid])[::-1]:
            print("逻辑不符合",Valid)
            print(''.join([str(i) for i in Valid]))
            print(reversed(''.join([str(i) for i in Valid])))
            return False
        else:

            print("正确")
            return True

    isValid("([)]",s="([)]")


'''
    以上方法仍然不成熟，使用栈才是最优解
    如何使用栈的思维处理该问题？
    基本操作：进栈 出栈

    栈先入后出特点恰好与本题括号排序特点一致，
    即若遇到左括号入栈，遇到右括号时将对应栈顶左括号出栈，
    则遍历完所有括号后 stack 仍然为空；
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            # 字符串的长度不符合偶数
            return False
        dic = {'{': '}',  '[': ']', '(': ')'}
        stack = []
        for c in s:
            # 左括号则入栈
            if c in dic: stack.append(c)
            # 
            elif c != dic[stack.pop()]: 
                return False 
        return len(stack) == 0
```



### 1006 - 合并两个有序链表<a id="p1006"></a>

#### 题目

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

**示例 1：**

![img](./assets/merge_ex1.jpg)

```
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
```

**示例 2：**

```
输入：l1 = [], l2 = []
输出：[]
```

**示例 3：**

```
输入：l1 = [], l2 = [0]
输出：[0]
```



#### 解法

初次解决链表问题，学会使用Python中的链表

```python
'''
    两个链表转化为列表
    直接进行排序
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tail = result
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        tail.next = list1 if list1 is not None else list2
        return result.next
```



### 1007 - 删除有序数组中的重复项<a id="p1007"></a>

#### 题目

给你一个 **非严格递增排列** 的数组 `nums` ，请你**[ 原地](http://baike.baidu.com/item/原地算法)** 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致** 。然后返回 `nums` 中唯一元素的个数。

考虑 `nums` 的唯一元素的数量为 `k` ，你需要做以下事情确保你的题解可以被通过：

- 更改数组 `nums` ，使 `nums` 的前 `k` 个元素包含唯一元素，并按照它们最初在 `nums` 中出现的顺序排列。`nums` 的其余元素与 `nums` 的大小不重要。
- 返回 `k` 。

**判题标准:**

系统会用下面的代码来测试你的题解:

```
int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

如果所有断言都通过，那么您的题解将被 **通过**。

 

**示例 1：**

```
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
```

**示例 2：**

```
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
```



#### 解法

对于列表可以转换为Set集合去重

```python
'''
    去重
    利用Set集合进行去重
    转换为List后再排序
'''
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums)  == 0: 
            return 0
        k =  1
        for  i in range(1, len(nums)):
             if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
```



### 1008 - 移除元素<a id="p1008"></a>

#### 问题

给你一个数组 `nums` 和一个值 `val`，你需要 **[原地](https://baike.baidu.com/item/原地算法)** 移除所有数值等于 `val` 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 `O(1)` 额外空间并 **[原地 ](https://baike.baidu.com/item/原地算法)修改输入数组**。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

 

**说明:**

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以**「引用」**方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

 

**示例 1：**

```
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
```

**示例 2：**

```
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,3,0,4]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
```



#### 解法

最终返回值是数组的长度

经典问题在于：
对于本体做出的删除操作，如空间复杂度为O(1)
在使用for循环(for i in nums)的条件下，对nums做出更改，实际上会产生错误：即(for i in nums)这一用法的底层实际上依然是(for i in range())

```python
# 朴素解法：计算nums中有多少符合条件的元素，再执行删除
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numofint = 0
        for i in nums:
            if i == val:
                numofint += 1
        for i in range(numofint):
            nums.remove(val)
        return len(nums)

# 错误解法：对于for循环的使用理解
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums:
            if i == val:
                nums.remove(i)
        return len(nums)

# 双指针解法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k =  1
        # for  i in range(1, len(nums)):
        #      if nums[i] != nums[i - 1]:
        #         nums[k] = nums[i]
        #         k += 1
        # return k
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return len(nums)

# while配合双指针解法，优于for+双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0
        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1
        return b
    
# 快慢指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
```



### 1009 - 找出字符串中第一个匹配项的下标<a id="p1009"></a>

#### 问题

给你两个字符串 `haystack` 和 `needle` ，请你在 `haystack` 字符串中找出 `needle` 字符串的第一个匹配项的下标（下标从 0 开始）。如果 `needle` 不是 `haystack` 的一部分，则返回 `-1` 。

 

**示例 1：**

```
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
```

**示例 2：**

```
输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
```



#### 解法

```python
'''
    字符串可以使用in方法
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            i = 0
            while True:
                if haystack[i:i + len(needle)] == needle:
                    return i
                i += 1
```



### 1010 - 搜索插入位置<a id="p1010"></a>

#### 问题

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

 

**示例 1:**

```
输入: nums = [1,3,5,6], target = 5
输出: 2
```

**示例 2:**

```
输入: nums = [1,3,5,6], target = 2
输出: 1
```

**示例 3:**

```
输入: nums = [1,3,5,6], target = 7
输出: 4
```



#### 解法

调库

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if target <= i:
                return nums.index(i)
        return len(nums)
```

二分法

问题：为什么最终返回left呢？

答：while循环终止，说明找不到或者已经返回了索引。所以此时left所在的位置就是要插入的位置。

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return left
```



### 1011 - 最后一个单词的长度<a id="p1011"></a>

#### 问题

给你一个字符串 `s`，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 **最后一个** 单词的长度。

**单词** 是指仅由字母组成、不包含任何空格字符的最大子字符串。

 

**示例 1：**

```
输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为5。
```

**示例 2：**

```
输入：s = "   fly me   to   the moon  "
输出：4
解释：最后一个单词是“moon”，长度为4。
```

**示例 3：**

```
输入：s = "luffy is still joyboy"
输出：6
解释：最后一个单词是长度为6的“joyboy”。
```



#### 解法

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
```



### 1012 - 加一<a id="p1012"></a>

#### 问题

给定一个由 **整数** 组成的 **非空** 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储**单个**数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

**示例 1：**

```
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
```

**示例 2：**

```
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
```

**示例 3：**

```
输入：digits = [0]
输出：[1]
```



#### 解法

```python
# 列表为主体
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else
            
        return digits
    
# 数据为主题
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 计算出该数字为多少:列表字符串转数字
        nums = ""
        while digits:
            nums = nums + str(digits.pop(0))
        nums = int(nums) + 1
        return [int(x) for x in str(nums)]
```



### 1013 - 二进制求和<a id="p1013"></a>

#### 问题

给你两个二进制字符串 `a` 和 `b` ，以二进制字符串的形式返回它们的和。

 

**示例 1：**

```
输入:a = "11", b = "1"
输出："100"
```

**示例 2：**

```
输入：a = "1010", b = "1011"
输出："10101"
```



#### 解法

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
```



### 1014 - x的平方根<a id="p1014"></a>

#### 问题

给你一个非负整数 `x` ，计算并返回 `x` 的 **算术平方根** 。

由于返回类型是整数，结果只保留 **整数部分** ，小数部分将被 **舍去 。**

**注意：**不允许使用任何内置指数函数和算符，例如 `pow(x, 0.5)` 或者 `x ** 0.5` 。

 

**示例 1：**

```
输入：x = 4
输出：2
```

**示例 2：**

```
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
```



#### 解法

```python
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.trunc(math.sqrt(x))
```



### 1015 - 爬楼梯<a id="p1015"></a>

#### 问题

假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。

每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

**示例 1：**

```
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
```

**示例 2：**

```
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
```



#### 解法

该题目涉及动态规划
使用数学思维：联想到斐波那契数列
建立数学函数：若爬上n层台阶，有f(n)种方法
其最后一次跳跃只有两种方法：跳一步和跳两步
所以f(n) = f(n - 1) + f(n - 2)
对于起步，很容易计算f(0) = 1,f(1) = 1
叠加即可计算

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a , b = 1 , 1
        for _ in range(n - 1):
            a , b = b , a + b
        return b
```



### 1016 - 删除排序链表中的重复元素<a id="p1016"></a>

#### 问题

给定一个已排序的链表的头 `head` ， *删除所有重复的元素，使每个元素只出现一次* 。返回 *已排序的链表* 。

 

**示例 1：**

![img](./assets/list1.jpg)

```
输入：head = [1,1,2]
输出：[1,2]
```

**示例 2：**

![img](./assets/list2.jpg)

```
输入：head = [1,1,2,3,3]
输出：[1,2,3]
```



#### 解法

非双指针解法，思想一致，但是少开辟了空间，节省了内存

注意：要正确的判断条件，且考虑周全

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        target = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return target
```

双指针解法

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        p = head
        q = p.next
        while q:
            if p.val == q.val:
                if q.next == None:
                    p.next = None
                    return head
                q = q.next
                p.next = q
            else:
                p = q
                q = q.next
        return head
```



### 1017 - 合并两个有序数组<a id="p1017"></a>

#### 问题

给你两个按 **非递减顺序** 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 **合并** `nums2` 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

**注意：**最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。`nums2` 的长度为 `n` 。

 

**示例 1：**

```
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
```

**示例 2：**

```
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
```

**示例 3：**

```
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
```



#### 解法

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 覆盖方法
        # for i in range(m,m + n):
        #     nums1[i] = nums2[i - m]
        # nums1.sort()

        # 双指针
        k = m - 1
        l = n - 1
        x = m + n - 1
        while k >= 0 and l >= 0:
            if nums1[k] >= nums2[l]:
                nums1[x] = nums1[k]
                k -= 1
            else:
                nums1[x] = nums2[l]
                l -= 1
            x -= 1
        while l >= 0:
            nums1[x] = nums2[l]
            l -= 1
            x -= 1 
```





### 1018 - 二叉树的中序遍历<a id="p1018"></a>

#### 问题

给定一个二叉树的根节点 `root` ，返回 *它的 **中序** 遍历* 。

 

**示例 1：**

![img](./assets/inorder_1.jpg)

```
输入：root = [1,null,2,3]
输出：[1,3,2]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [1]
输出：[1]
```



#### 解法

方法一：使用递归方法

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        def demo(target:Optional[TreeNode]):
            if target:
                demo(target.left)
                result.append(target.val)
                demo(target.right)
        demo(root)
        return result
```

方法二：使用迭代解法

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        temp = []
        result = []
        while root or temp:
            if root:
                temp.append(root)
                root = root.left
            else:
                temp1 = temp.pop()
                result.append(temp1.val)
                root = temp1.right
        return result
```



### 1019 - 相同的树<a id="p1019"></a>

#### 问题

给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

 

**示例 1：**

![img](./assets/ex1.jpg)

```
输入：p = [1,2,3], q = [1,2,3]
输出：true
```

**示例 2：**

![img](./assets/ex2.jpg)

```
输入：p = [1,2], q = [1,null,2]
输出：false
```

**示例 3：**

![img](./assets/ex3.jpg)

```
输入：p = [1,2,1], q = [1,1,2]
输出：false
```



#### 解法

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
```



### 1020 - 对称二叉树<a id="p1020"></a>

#### 问题

给你一个二叉树的根节点 `root` ， 检查它是否轴对称。

 

**示例 1：**

![img](./assets/1698026966-JDYPDU-image.png)

```
输入：root = [1,2,2,3,4,4,3]
输出：true
```

**示例 2：**

![img](./assets/1698027008-nPFLbM-image.png)

```
输入：root = [1,2,2,null,3,null,3]
输出：false
```



#### 解法

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def judge(self,rootleft:Optional[TreeNode],rootright:Optional[TreeNode]) -> bool:
            if not rootleft and not rootright:
                return True
            if not rootleft or not rootright:
                return False
            if rootleft.val != rootright.val:
                return False
            else:
                return self.judge(rootleft.left,rootright.right) and self.judge(rootleft.right,rootright.left)
            return True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.judge(root.left,root.right)
```



### 1021 - 二叉树的最大深度<a id="p1021"></a>

#### 问题

给定一个二叉树 `root` ，返回其最大深度。

二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

 

**示例 1：**

![img](./assets/tmp-tree.jpg)

 

```
输入：root = [3,9,20,null,null,15,7]
输出：3
```

**示例 2：**

```
输入：root = [1,null,2]
输出：2
```



#### 解法

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Judge(self, root) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and root.right:
            return max(1 + self.Judge(root.left),1 + self.Judge(root.right))
        elif root.left or root.right:
            return max((1 + self.Judge(root.left)),(1 + self.Judge(root.right)))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.Judge(root)
```



### 1022 - 将有序数组转换为二叉搜索树<a id="p1022"></a>

#### 问题

给你一个整数数组 `nums` ，其中元素已经按 **升序** 排列，请你将其转换为一棵 **高度平衡** 二叉搜索树。

**高度平衡** 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

 

**示例 1：**

![img](./assets/btree1.jpg)

```
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
```

**示例 2：**

![img](./assets/btree.jpg)

```
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
```



#### 解法

递归创建二叉树，难点在于要平衡，所以要均分左右

其实只要每次寻找中间值就好

精妙之处在于无论奇数偶数，计算出的中间节点都是一样的：四舍五入；比如6和7

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        lenth = len(nums)
        # 二叉搜索树，左子树比根节点小，右子树比根节点大
        # 每次二分 递归
        # 创建二叉树
        def createTree(l , r) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            tree = TreeNode(nums[mid])
            tree.left = createTree(l,mid - 1)
            tree.right = createTree(mid + 1,r)
            return tree
        return createTree(0,lenth - 1)
```



### 1023 - 平衡二叉树<a id="p1023"></a>

#### 问题

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

> 一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过 1 。

 

**示例 1：**

![img](./assets/balance_1.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：true
```

**示例 2：**

![img](./assets/balance_2.jpg)

```
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
```

**示例 3：**

```
输入：root = []
输出：true
```



#### 解法

普通方法：

lenth方法用来计算树的深度

再判断左右树的深度差绝对值即可。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left 
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 判断的是每个节点的左右子树的高度差
        # 而不是整棵树最高节点和最低节点的高度差
        # 将树分为左右，判断左右即可
        def lenth(root) -> int:
            if not root:
                return 0
            elif not root.left and not root.right:
                return 1
            elif root.left and root.right:
                return max(1 + lenth(root.left),1 + lenth(root.right))
            elif root.left or root.right:
                return max((1 + lenth(root.left)),(1 + lenth(root.right)))
        def Judge(root):
            if not root or (not root.left and not root.right):
                return True
            if abs(lenth(root.left) - lenth(root.right)) > 1:
                return False
            else:
                return Judge(root.left) and Judge(root.right)
        return Judge(root)
```

剪枝法：

该方法即使用了最简单的方法统计了树的高度，同时还可以判定树是否为平衡二叉树。

对于recur函数，其有两个作用：1.探查树的深度 2.判断树是否为平衡树

关于其第一个作用不做解释，就是判断深度。

但是其第二个作用的实现，很为精妙：首先，`if left == -1: return -1`和`if right == -1: return -1`两句，实现的功能是，一旦发现有不平衡的部分，则全局返回-1来判断此树不是平衡树；其次，其每次探查完左右子树的长度后立即比对是否为平衡树，可以立即返回结果；最后，这种极为巧妙地层级设计帮助一旦遇到非平衡情况能全局返回最终结果。

对待这个函数要全局来看：仅从第一层来看的话，其比较的是左右两侧的最大值的长度，直觉上不能比较是否平衡，但是实际上，其完全遍历了树的左右，是正确的。

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
```



### 1024 - 二叉树的最小深度<a id="p1024"></a>

#### 问题

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

**说明：**叶子节点是指没有子节点的节点。

 

**示例 1：**

![img](./assets/ex_depth.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：2
```

**示例 2：**

```
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
```



#### 解法

递归：

整棵树遍历返回最小深度

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.right) + 1,self.minDepth(root.left) + 1)
        return self.minDepth(root) + 1
```

迭代：

该迭代方法中，使用了栈（列表）储存元组的方法，每次读取列表中最后的元组，来记录深度和节点对象（中间值）。

直到最先找到某个节点是叶子节点即可：最先找到的必定最小。

```python
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        deque = []
        deque.append((1, root))
        
        while deque:
            depth, root = deque.pop(0) 
            # 判断是否是叶子节点
            if not root.left and not root.right:
                return depth    
            # 非空记录节点+深度
            if root.left:deque.append((depth+1, root.left))
            if root.right:deque.append((depth+1, root.right))
```



### 1025 - 路径总和<a id="p1025"></a>

#### 问题

给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。

**叶子节点** 是指没有子节点的节点。

 

**示例 1：**

![img](./assets/pathsum1.jpg)

```
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
```

**示例 2：**

![img](./assets/pathsum2.jpg)

```
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
```

**示例 3：**

```
输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。
```



#### 解法

递归，找到某个路径的节点总和是否为某个特定值，可以将问题转化为是否有一条路可以在到达叶子节点的时候将目标值减为0。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        else:
            if root.left and root.right:
                return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
            elif not root.left and not root.right and targetSum - root.val == 0:
                return True
            else:
                return self.hasPathSum(root.left, targetSum - root.val) if root.left else self.hasPathSum(root.right, targetSum - root.val)
```



### 1026 - 杨辉三角<a id="p1026"></a>

#### 问题

给定一个非负整数 *`numRows`，*生成「杨辉三角」的前 *`numRows`* 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

![img](./assets/1626927345-DZmfxB-PascalTriangleAnimated2.gif)

 

**示例 1:**

```
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**示例 2:**

```
输入: numRows = 1
输出: [[1]]
```



#### 解法

杨辉三角的一个特点是：左右恒为1

而且其某层的元素就是上一个列表的相邻值相加得来，所以核心代码在于根据上一层计算出下一层

有意思的是：解决杨辉三角每层左右都是1的方法是先添加1，执行完核心代码再添加1

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 最左和最右 + 1
        # 每次将上层列表的值 求和
        result = [[1]]
        for i in range(1, numRows):
            temp = [1]
            # 获取上层列表
            last_lst = result[i - 1]
            for j in range(1, len(last_lst)):
                temp.append(last_lst[j] + last_lst[j - 1])
            temp.append(1)
            result.append(temp)
        return result
```



### 1027 - 杨辉三角 II<a id="p1027"></a>

#### 问题

给定一个非负索引 `rowIndex`，返回「杨辉三角」的第 `rowIndex` 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

![img](./assets/1626927345-DZmfxB-PascalTriangleAnimated2-1709296357890-7.gif)

 

**示例 1:**

```
输入: rowIndex = 3
输出: [1,3,3,1]
```

**示例 2:**

```
输入: rowIndex = 0
输出: [1]
```

**示例 3:**

```
输入: rowIndex = 1
输出: [1,1]
```



#### 解法

比上一题多计算一层并返回最后一层即可

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 最左和最右 + 1
        # 每次将上层列表的值 求和
        result = [[1]]
        for i in range(1, rowIndex + 1):
            temp = [1]
            # 获取上层列表
            last_lst = result[i - 1]
            for j in range(1, len(last_lst)):
                temp.append(last_lst[j] + last_lst[j - 1])
            temp.append(1)
            result.append(temp)
        return result[-1]
```



### 1028 - 买卖股票的最佳时机<a id="p1028"></a>

#### 问题

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

 

**示例 1：**

```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

**示例 2：**

```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```



#### 解法

本题暴力解法最简单，但是很容易超时

方法一：很好理解，每次记录自遍历开始的最低价格和最大差值

其中，先获得最低价格后再计算最大差值，可以保证永远不会减出负数，避免了高买低出

方法二：方法二精髓在于相较于方法一减小了计算量，其核心思想是，假设第一天为最低价格，向后遍历，遇到更低的价格就将更新最低价格，遇到不是最低的价格就直接使用今日价格减最低价格获得答案，答案随着遍历更新。

至于其减少的计算量就是：方法一在最低价格更新后还会相减一次，结果必为0，没有意义。

```python
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 锚定某天买入，推以后最大值卖出
#         # 暴力解法：超时
#         lenth = len(prices)
#         lst = []
#         for i in range(lenth):
#             lst.append(max(prices[j] for j in range(i, lenth)) - prices[i])
#         return max(lst)

# 方法一
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit

# 方法二
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ans=0
        curmin=prices[0]
        for i,v in enumerate(prices):
            if v<curmin:
                curmin=v
            else:
                ans=max(ans, v-curmin)
        return ans
```



### 1029 - 验证回文串<a id="p1029"></a>

#### 问题

如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 **回文串** 。

字母和数字都属于字母数字字符。

给你一个字符串 `s`，如果它是 **回文串** ，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
```

**示例 2：**

```
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
```

**示例 3：**

```
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
```



#### 解法

两种方法区别在于如何校验是否是回文串

目前调库快于双指针

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 调库高手:更快
        # 处理字符串：根据ASCII码，只加入字母，对大写字母处理
        lst = []
        for i in s:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
                lst.append(i)
            elif ord(i) >= 65 and ord(i) <= 90:
                lst.append(chr(ord(i) + 32))
        
        new_s = "".join(lst)
        return new_s == new_s[::-1]

        # 双指针
        lst = []
        for i in s:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
                lst.append(i)
            elif ord(i) >= 65 and ord(i) <= 90:
                lst.append(chr(ord(i) + 32))

        lenth = len(lst)
        for i in range(lenth // 2):
            if lst[i] == lst[lenth - 1]:
                lenth -= 1
            else:
                return False
        return True
```



### 1030 - 只出现一次的数字<a id="p1030"></a>

#### 问题

给你一个 **非空** 整数数组 `nums` ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

 

**示例 1 ：**

```
输入：nums = [2,2,1]
输出：1
```

**示例 2 ：**

```
输入：nums = [4,1,2,1,2]
输出：4
```

**示例 3 ：**

```
输入：nums = [1]
输出：1
```



#### 解法

位运算：对二进制形式的数字进行位运算，如果两个数字相同则返回0，如果不同则返回两个二进制数的不同之处（由两个二进制数字的1填充）

异或运算的精髓在于：其符合交换律，比如a ^ b = b ^ a。

对于本题目而言：若出现数组[2, 2, 1, 4, 4]，无需在意1 ^ 4的结果，因为最后其还要有1 ^ 4 ^ 4 运算，最终结果还是1。

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 暴力破解
        # 10%
        lenth = len(nums)
        if lenth == 1:
            return nums[0]
        lst = []
        for i in range(lenth):
            if nums[i] not in lst:
                lst.append(nums[i])
            else:
                lst.remove(nums[i])
        return lst[0]

        # 位运算
        lenth = len(nums)
        if lenth == 1: return nums[0]
        result = nums[0]
        for i in range(1, lenth):
            result = result ^ nums[i]
        return result
```



### 1031 - 环形链表<a id="p1031"></a>

#### 问题

给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：`pos` 不作为参数进行传递** 。仅仅是为了标识链表的实际情况。

*如果链表中存在环* ，则返回 `true` 。 否则，返回 `false` 。

 

**示例 1：**

![img](./assets/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

![img](./assets/circularlinkedlist_test2.png)

```
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

![img](./assets/circularlinkedlist_test3.png)

```
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```



#### 解法

暴力解法：数据量有范围，选最大范围处理即可。

双指针解法：快的指针终将追上慢的指针，它们之间的相对距离以1的距离缩减。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 暴力解法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        while index < 10001:
            if not head:
                return False
            head = head.next
            index += 1
        return True

# 快慢指针：快的指针必定会追上慢的指针
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next
            if fast == slow:
                return True
        return False
```



### 1032 - 二叉树的前序遍历<a id="p1032"></a>

#### 问题

给你二叉树的根节点 `root` ，返回它节点值的 **前序** 遍历。

 

**示例 1：**

![img](./assets/inorder_1-1709551183284-1.jpg)

```
输入：root = [1,null,2,3]
输出：[1,2,3]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [1]
输出：[1]
```

**示例 4：**

![img](./assets/inorder_5.jpg)

```
输入：root = [1,2]
输出：[1,2]
```

**示例 5：**

![img](./assets/inorder_4.jpg)

```
输入：root = [1,null,2]
输出：[1,2]
```

 

**提示：**

- 树中节点数目在范围 `[0, 100]` 内
- `-100 <= Node.val <= 100`

 

**进阶：**递归算法很简单，你可以通过迭代算法完成吗？



#### 解法

递归

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(root: Optional[TreeNode]):
            if not root:
                return
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return result
```



### 1033 - 二叉树的后序遍历<a id="p1033"></a>

#### 问题

给你一棵二叉树的根节点 `root` ，返回其节点值的 **后序遍历** 。

 

**示例 1：**

![img](./assets/pre1.jpg)

```
输入：root = [1,null,2,3]
输出：[3,2,1]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [1]
输出：[1]
```

 

**提示：**

- 树中节点的数目在范围 `[0, 100]` 内
- `-100 <= Node.val <= 100`

 

**进阶：**递归算法很简单，你可以通过迭代算法完成吗？



#### 解法

递归

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def posoder(root: Optional[TreeNode]):
            if root and root.left:
                posoder(root.left)
            if root and root.right:
                posoder(root.right)
            if root:
                lst.append(root.val)
        posoder(root)
        return lst
```



### 1034 - 两数之和<a id="p1034"></a>

#### 问题

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

**示例 1：**

![img](./assets/addtwonumber1.jpg)

```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
```

**示例 2：**

```
输入：l1 = [0], l2 = [0]
输出：[0]
```

**示例 3：**

```
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
```



#### 解法

思路
将两个链表转换成长度相等的两数相加，在短链表前补0，例如123+1转换成123+001=124。而由于本题中链表是逆序存储数字的，因此是在链表的尾部补0。之后，类似于手写竖式加法，逐位相加，记录每位的进位与余数即可。

解法
在链表题中，常用的方法是先定义一个dummy节点，这样可以避免对头节点的特殊处理。需要注意的是，在遍历结束后，如果carry不为0，需要在链表最后增加一个节点，例如99+01=100，结果100中的1就是最后的进位。

```python
# 增补法
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        res = result
        jw = 0
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + jw
            jw = sum // 10
            res.next = ListNode(sum - 10 if sum >= 10 else sum)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if jw:
            res.next = ListNode(1)
        return result.next
```



### 1035 - 二分查找<a id="p1035"></a>

#### 问题

给定一个 `n` 个元素有序的（升序）整型数组 `nums` 和一个目标值 `target` ，写一个函数搜索 `nums` 中的 `target`，如果目标值存在返回下标，否则返回 `-1`。


**示例 1:**

```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
```

**示例 2:**

```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```



#### 解法

调库

```python
# 调库
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
```

正常写法

```python
# 正常写法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lenth = len(nums)
        head = lenth - 1
        tail = 0
        while True:
            if head < tail:
                return -1
            mid = (head - tail) // 2 + tail
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                head = mid - 1
            elif nums[mid] < target:
                tail = mid + 1
```



### 1036 - 反转字符串<a id="p1036"></a>

#### 问题

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 `s` 的形式给出。

不要给另外的数组分配额外的空间，你必须**[原地](https://baike.baidu.com/item/原地算法)修改输入数组**、使用 O(1) 的额外空间解决这一问题。

 

**示例 1：**

```
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
```

**示例 2：**

```
输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```



#### 解法

双指针解法

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 双指针
        tail, head = 0, len(s) - 1
        for i in range(head + 1):
            if head <= tail:
                break
            temp = s[tail]
            s[tail] = s[head]
            s[head] = temp
            tail, head = tail + 1, head - 1
```

调库

对于使用`[::-1]`切片方法其本质上是返回一个新的数组，而是用`reverse`方法则是直接在内存上做出修改。

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 调库
        return s.reverse()
```





### 1037 - 反转字符串 II<a id="p1037"></a>

#### 问题

给定一个字符串 `s` 和一个整数 `k`，从字符串开头算起，每计数至 `2k` 个字符，就反转这 `2k` 字符中的前 `k` 个字符。

- 如果剩余字符少于 `k` 个，则将剩余字符全部反转。
- 如果剩余字符小于 `2k` 但大于或等于 `k` 个，则反转前 `k` 个字符，其余字符保持原样。

 

**示例 1：**

```
输入：s = "abcdefg", k = 2
输出："bacdfeg"
```

**示例 2：**

```
输入：s = "abcd", k = 2
输出："bacd"
```



#### 解法

普通解法

```python
# 每隔着k个字符记录，反转偶数数
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = []
        temp = []
        for i in range(len(s)):
            if i % k == 0:
                lst.append(temp)
                temp = []
            temp.append(s[i])
        if temp:
            lst.append(temp)
        lst.pop(0)
        result = ""
        for i in range(len(lst)):
            temp = ""
            for char in lst[i]:
                temp = temp + char
            if i % 2 == 0:
                result = result + temp[::-1]
            else:
                result = result + temp
        return result
```

字符串拼接

```python
# 利用python对于字符串可操作的特性
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = s[k - 1::-1] + s[k:]
        for i in range(2 * k, len(s), 2 * k):
            s = s[0:i:] + s[i + k - 1:i - 1:-1] + s[i + k:len(s):]
        return s
```

简写

```python
# 简写
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return "".join(s[i:i + k][::(-1 if i // k % 2 == 0 else 1)] for i in range(0, len(s), k))
```



### 1038 - 有序数组的平方<a id="p1038"></a>

#### 问题

给你一个按 **非递减顺序** 排序的整数数组 `nums`，返回 **每个数字的平方** 组成的新数组，要求也按 **非递减顺序** 排序。



**示例 1：**

```
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
```

**示例 2：**

```
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
```



#### 解法

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 调库
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums

        # 双指针
        l, r, k = 0, len(nums) - 1, len(nums) - 1
        result = [0] * len(nums)
        while k >= 0:
            if nums[l] * nums[l] >= nums[r] * nums[r]:
                result[k] = nums[l] * nums[l]
                l += 1
            else:
                result[k] = nums[r] * nums[r]
                r -= 1
            k -= 1
        return result
```



### 1039 - 密钥格式化<a id="p1039"></a>

#### 问题

给定一个许可密钥字符串 `s`，仅由字母、数字字符和破折号组成。字符串由 `n` 个破折号分成 `n + 1` 组。你也会得到一个整数 `k` 。

我们想要重新格式化字符串 `s`，使每一组包含 `k` 个字符，除了第一组，它可以比 `k` 短，但仍然必须包含至少一个字符。此外，两组之间必须插入破折号，并且应该将所有小写字母转换为大写字母。

返回 *重新格式化的许可密钥* 。

 

**示例 1：**

```
输入：S = "5F3Z-2e-9-w", k = 4
输出："5F3Z-2E9W"
解释：字符串 S 被分成了两个部分，每部分 4 个字符；
     注意，两个额外的破折号需要删掉。
```

**示例 2：**

```
输入：S = "2-5g-3-J", k = 2
输出："2-5G-3J"
解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
```



#### 解法

调库

```python
# 字符串
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace('-', '')[::-1]
        nub = 0
        res = ''
        for i in range(0, len(s), k):
            res += s[i:i+k] + '-'
        return res[::-1].lstrip('-')
```



### 1040 - 长度最小的子数组<a id="p1040"></a>

#### 问题

给定一个含有 `n` 个正整数的数组和一个正整数 `target` **。**

找出该数组中满足其总和大于等于 `target` 的长度最小的 **连续子数组** `[numsl, numsl+1, ..., numsr-1, numsr]` ，并返回其长度**。**如果不存在符合条件的子数组，返回 `0` 。

 

**示例 1：**

```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```

**示例 2：**

```
输入：target = 4, nums = [1,4,4]
输出：1
```

**示例 3：**

```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```



#### 解法

滑动窗口方法

窗口的起始位置如何移动：如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）。

窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，也就是for循环里的索引。

**滑动窗口的精妙之处在于根据当前子序列和大小的情况，不断调节子序列的起始位置。**

内部的while也是高明的地方：当累加值大于目标值后的处理，即左侧指针可能不止要移动一次。

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0 #当前的累加值
        
        while right < l:
            cur_sum += nums[right]
            
            while cur_sum >= s: # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1
        
        return min_len if min_len != float('inf') else 0
```



### 1041 - 螺旋矩阵 II<a id="#p1041"></a>

#### 问题

给你一个正整数 `n` ，生成一个包含 `1` 到 `n2` 所有元素，且元素按顺时针顺序螺旋排列的 `n x n` 正方形矩阵 `matrix` 。

 

**示例 1：**

![img](./assets/spiraln.jpg)

```
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
```

**示例 2：**

```
输入：n = 1
输出：[[1]]
```



#### 解法

```python
# 模拟过程
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 外层每次遍历的长度实际上是n - 1
        # 遍历完一层之后，下一层遍历的长度为 - 1
        # 模拟的顺序为：右  下  左  上
        max_lenth = n - 1    # 阈值
        result = [[-1 for _ in range(n)] for _ in range(n)]   # 初始化列表
        x, y = 0, 0     # 代表遍历坐标
        num = 1     # 需要叠加的值
        while max_lenth > 0:
            # 向右遍历
            for i in range(max_lenth):
                result[x][y] = num
                num += 1
                y += 1
            # 向下遍历
            for i in range(max_lenth):
                result[x][y] = num
                num += 1
                x += 1
            # 向左遍历
            for i in range(max_lenth):
                result[x][y] = num
                num += 1
                y -= 1
            # 向上遍历
            for i in range(max_lenth):
                result[x][y] = num
                num += 1
                x -= 1
            x += 1
            y += 1
            max_lenth -= 2
        if n % 2:
            result[n // 2][n // 2] = num
        return result
```



### 1042 - 移除链表元素<a id="p1042"></a>

#### 问题

给你一个链表的头节点 `head` 和一个整数 `val` ，请你删除链表中所有满足 `Node.val == val` 的节点，并返回 **新的头节点** 。

 

**示例 1：**

![img](./assets/removelinked-list.jpg)

```
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
```

**示例 2：**

```
输入：head = [], val = 1
输出：[]
```

**示例 3：**

```
输入：head = [7,7,7,7], val = 7
输出：[]
```



#### 解法

```python
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        result = ListNode(next = head)
        head = result
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        
        return result.next
```



### 1043 - 设计链表<a id="p1043"></a>

#### 问题

你可以选择使用单链表或者双链表，设计并实现自己的链表。

单链表中的节点应该具备两个属性：`val` 和 `next` 。`val` 是当前节点的值，`next` 是指向下一个节点的指针/引用。

如果是双向链表，则还需要属性 `prev` 以指示链表中的上一个节点。假设链表中的所有节点下标从 **0** 开始。

实现 `MyLinkedList` 类：

- `MyLinkedList()` 初始化 `MyLinkedList` 对象。
- `int get(int index)` 获取链表中下标为 `index` 的节点的值。如果下标无效，则返回 `-1` 。
- `void addAtHead(int val)` 将一个值为 `val` 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
- `void addAtTail(int val)` 将一个值为 `val` 的节点追加到链表中作为链表的最后一个元素。
- `void addAtIndex(int index, int val)` 将一个值为 `val` 的节点插入到链表中下标为 `index` 的节点之前。如果 `index` 等于链表的长度，那么该节点会被追加到链表的末尾。如果 `index` 比长度更大，该节点将 **不会插入** 到链表中。
- `void deleteAtIndex(int index)` 如果下标有效，则删除链表中下标为 `index` 的节点。

 

**示例：**

```
输入
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
输出
[null, null, null, null, 2, null, 3]

解释
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
myLinkedList.get(1);              // 返回 2
myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
myLinkedList.get(1);              // 返回 3
```



#### 解法

```python
class Node:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        prenode = Node()
        self.head = prenode

    def get(self, index: int) -> int:
        # 根据索引获取当前的值
        headnode = self.head.next
        while index > 0:
            if not headnode:
                return -1
            headnode = headnode.next
            index -= 1
        if not headnode:
            return -1
        return headnode.val

    def addAtHead(self, val: int) -> None:
        # 增添头节点
        prenode = self.head
        temp = Node(val=val)
        temp.next = prenode.next
        prenode.next = temp

    def addAtTail(self, val: int) -> None:
        # 添加尾节点
        headnode = self.head
        while headnode and headnode.next:
            headnode = headnode.next
        headnode.next = Node(val = val)

    def addAtIndex(self, index: int, val: int) -> None:
        # 根据索引添加元素：如果 index 比长度更大，该节点将 不会插入 到链表中。
        headnode = self.head    # 此处代表虚拟节点
        for i in range(index):
            if not headnode:
                return
            headnode = headnode.next
        if not headnode:
            return
        temp = Node(val, headnode.next if headnode.next else None)
        headnode.next = temp
        

    def deleteAtIndex(self, index: int) -> None:
        # 根据索引删除元素：如果下标有效，则删除链表中下标为 index 的节点。
        # 三种情况：删除正常元素、删除最后一个元素、删除越界节点
        headnode = self.head    # 此处代表虚拟节点
        for i in range(index):
            if not headnode:
                return
            headnode = headnode.next
        if not headnode:
            return
        elif headnode and not headnode.next:
            headnode.next = None
        else:
            headnode.next = headnode.next.next
```



### 1044 - 反转链表<a id="p1043"></a>

#### 问题

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

 

**示例 1：**

![img](./assets/rev1ex1.jpg)

```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

**示例 2：**

![img](./assets/rev1ex2.jpg)

```
输入：head = [1,2]
输出：[2,1]
```

**示例 3：**

```
输入：head = []
输出：[]
```



#### 解法

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 三指针
        next_node = head.next
        head.next = None
        while next_node:
            temp = next_node.next
            next_node.next = head
            head = next_node
            next_node = temp
        return head
```



### 1045 - 两两交换链表中的节点<a id="p1045"></a>

#### 问题

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

**示例 1：**

![img](./assets/swap_ex1.jpg)

```
输入：head = [1,2,3,4]
输出：[2,1,4,3]
```

**示例 2：**

```
输入：head = []
输出：[]
```

**示例 3：**

```
输入：head = [1]
输出：[1]
```



#### 解法

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # while循环判断条件，遇到head为空或next为空终止即可
        if not head or not head.next:
            return head
        result = head.next
        last_temp = ListNode()
        while head and head.next:
            temp = head.next
            last_temp.next = temp
            head.next = temp.next
            last_temp = head
            temp.next = head
            head = head.next
        return result
```



### 1046 - 删除链表的倒数第N个节点<a id="p1046"></a>

#### 问题

给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

 

**示例 1：**

![img](./assets/remove_ex1.jpg)

```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

**示例 2：**

```
输入：head = [1], n = 1
输出：[]
```

**示例 3：**

```
输入：head = [1,2], n = 1
输出：[1]
```



#### 解法

快慢指针

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # fast要比slow快 n + 1 步
        Prenode = ListNode(next = head)
        result = Prenode
        fast = head
        while n - 1:
            fast = fast.next
            n = n - 1
        while fast.next:
            Prenode = Prenode.next
            fast = fast.next
        Prenode.next = Prenode.next.next
        return result.next
```



### 1047 - 链表相交<a id="p1046"></a>

#### 问题

给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 `null` 。

图示两个链表在节点 `c1` 开始相交**：**

[![img](./assets/160_statement.png)](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

题目数据 **保证** 整个链式结构中不存在环。

**注意**，函数返回结果后，链表必须 **保持其原始结构** 。

 

**示例 1：**

[![img](./assets/160_example_1.png)](https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png)

```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
```

**示例 2：**

[![img](./assets/160_example_2.png)](https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png)

```
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

**示例 3：**

[![img](./assets/160_example_3.png)](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)

```
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
```



#### 解法

求长度后，从距离尾部等长的位置遍历

代码随想录：

简单来说，就是求两个链表交点节点的**指针**。 这里同学们要注意，交点不是数值相等，而是指针相等。

为了方便举例，假设节点元素数值相等，则节点指针相等。

看如下两个链表，目前curA指向链表A的头结点，curB指向链表B的头结点：

![面试题02.07.链表相交_1](./assets/面试题02.07.链表相交_1.png)

我们求出两个链表的长度，并求出两个链表长度的差值，然后让curA移动到，和curB 末尾对齐的位置，如图：

![面试题02.07.链表相交_2](./assets/面试题02.07.链表相交_2.png)

此时我们就可以比较curA和curB是否相同，如果不相同，同时向后移动curA和curB，如果遇到curA == curB，则找到交点。

否则循环退出返回空指针。

```python
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curA = headA;
        ListNode* curB = headB;
        int lenA = 0, lenB = 0;
        while (curA != NULL) { // 求链表A的长度
            lenA++;
            curA = curA->next;
        }
        while (curB != NULL) { // 求链表B的长度
            lenB++;
            curB = curB->next;
        }
        curA = headA;
        curB = headB;
        // 让curA为最长链表的头，lenA为其长度
        if (lenB > lenA) {
            swap (lenA, lenB);
            swap (curA, curB);
        }
        // 求长度差
        int gap = lenA - lenB;
        // 让curA和curB在同一起点上（末尾位置对齐）
        while (gap--) {
            curA = curA->next;
        }
        // 遍历curA 和 curB，遇到相同则直接返回
        while (curA != NULL) {
            if (curA == curB) {
                return curA;
            }
            curA = curA->next;
            curB = curB->next;
        }
        return NULL;
    }
};
```

莫比乌斯环：一个链表到尾部后反转到另一个链表的头部，最终即便两个链表不等长，也会弥补。

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 处理边缘情况
        if not headA or not headB:
            return None
        
        # 在每个链表的头部初始化两个指针
        pointerA = headA
        pointerB = headB
        
        # 遍历两个链表直到指针相交
        while pointerA != pointerB:
            # 将指针向前移动一个节点
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        # 如果相交，指针将位于交点节点，如果没有交点，值为None
        return pointerA
```



### 1048 - 环形链表 II<a id="p1048"></a>

#### 问题

给定一个链表的头节点  `head` ，返回链表开始入环的第一个节点。 *如果链表无环，则返回 `null`。*

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（**索引从 0 开始**）。如果 `pos` 是 `-1`，则在该链表中没有环。**注意：`pos` 不作为参数进行传递**，仅仅是为了标识链表的实际情况。

**不允许修改** 链表。



 

**示例 1：**

![img](./assets/circularlinkedlist-1709788115895-15.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

![img](./assets/circularlinkedlist_test2-1709788115896-17.png)

```
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

![img](./assets/circularlinkedlist_test3-1709788115896-19.png)

```
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
```



#### 解法

暴力解法：遍历一遍，将所有的结点加入哈希表，对比即可

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 暴力，使用哈希表
        hashset = set()
        while head:
            if head in hashset:
                return head
            else:
                hashset.add(head)
            head = head.next
        return None
```

快慢指针，经过数学推导：找到相遇结点之后，从起始结点和相遇结点各自发出一个指针，相遇后必定为环形入口。

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针
        if not head:
            return None
        fast = slow = Prenode = ListNode(next = head)
        love_point = None
        while fast and fast.next and fast.next.next:
            if fast == slow and fast != Prenode:
                love_point = slow
                while Prenode != love_point:
                    Prenode = Prenode.next
                    love_point = love_point.next
                return love_point
            slow = slow.next
            fast = fast.next.next

        return None
```



### 1049 - 有效的字母异位词<a id="p1049"></a>

#### 问题

给定两个字符串 `*s*` 和 `*t*` ，编写一个函数来判断 `*t*` 是否是 `*s*` 的字母异位词。

**注意：**若 `*s*` 和 `*t*` 中每个字符出现的次数都相同，则称 `*s*` 和 `*t*` 互为字母异位词。

 

**示例 1:**

```
输入: s = "anagram", t = "nagaram"
输出: true
```

**示例 2:**

```
输入: s = "rat", t = "car"
输出: false
```



#### 解法

哈希表对比：即便键值对的位置不同但是仍然是一样的。

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 使用字典处理，即便是字典键值对位置不同依然是相等的
        dirt1, dirt2 = {}, {}
        for i in s:
            if i in dirt1:
                dirt1[i] = dirt1[i] + 1
            else:
                dirt1.setdefault(i, 1)

        for i in t:
            if i in dirt2:
                dirt2[i] = dirt2[i] + 1
            else:
                dirt2.setdefault(i, 1)

        return dirt1 == dirt2
```

使用`collections.defaultdict()` 类

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1
        
        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict
```



### 1050 - 两个数组的交集<a id="p1050"></a>

#### 问题

给定两个数组 `nums1` 和 `nums2` ，返回 *它们的交集* 。输出结果中的每个元素一定是 **唯一** 的。我们可以 **不考虑输出结果的顺序** 。

 

**示例 1：**

```
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
```

**示例 2：**

```
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
```



#### 解法

普通暴力解法

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 暴力
        new_set = set()
        for i in nums1:
            if i in nums2:
                new_set.add(i)
        return list(new_set)
```

集合直接取交集操作

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set之间使用位运算符可以实现并集、交集的操作
        return list(set(nums1) & set(nums2))
```



### 1051 - 快乐数<a id="p1051"></a>

#### 问题

编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」** 定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
- 然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。
- 如果这个过程 **结果为** 1，那么这个数就是快乐数。

如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

 

**示例 1：**

```
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

**示例 2：**

```
输入：n = 2
输出：false
```



#### 解法

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        # 经过数学演算，如果是无限循环，也是有规律的循环：即还会回到最初值
        lst = [n]
        while True:
            next_num = 0
            if n == 1:
                return True
            for i in str(n):
                next_num += int(i) * int(i)
            n = next_num
            if next_num not in lst:
                lst.append(next_num)
            else:
                return False
```



### 1052 - 四数相加 II<a id="p1052"></a>

#### 问题

给你四个整数数组 `nums1`、`nums2`、`nums3` 和 `nums4` ，数组长度都是 `n` ，请你计算有多少个元组 `(i, j, k, l)` 能满足：

- `0 <= i, j, k, l < n`
- `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`

 

**示例 1：**

```
输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
两个元组如下：
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
```

**示例 2：**

```
输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
输出：1
```



#### 解法

分段处理，将A、B数组的和统计，和作为键，出现次数为值；以相同的方式遍历C、D，一旦发现和的负数存在于字典中就将对应的值累加到结果。

```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 转换思路，先统计a + b的和出现的次数
        # 再统计c + d的和的次数
        # 将相减为0的次数相乘，累加
        dirt1, dirt2 = {}, {}
        result = 0
        for i in nums1:
            for j in nums2:
                temp = i + j
                if temp in dirt1:
                    dirt1[temp] += 1
                else:
                    dirt1[temp] = 1

        for k in nums3:
            for l in nums4:
                temp = -(k + l)
                if temp in dirt1:
                    result += dirt1[temp]

        return result
```



### 1053 - 赎金信<a id="p1053"></a>

#### 问题

给你两个字符串：`ransomNote` 和 `magazine` ，判断 `ransomNote` 能不能由 `magazine` 里面的字符构成。

如果可以，返回 `true` ；否则返回 `false` 。

`magazine` 中的每个字符只能在 `ransomNote` 中使用一次。

 

**示例 1：**

```
输入：ransomNote = "a", magazine = "b"
输出：false
```

**示例 2：**

```
输入：ransomNote = "aa", magazine = "ab"
输出：false
```

**示例 3：**

```
输入：ransomNote = "aa", magazine = "aab"
输出：true
```



#### 解法

将magazine出现的字符以及次数记录在字典中，遍历rensonNote中的字符，如果不存在就返回否，如果字典的值为0就删掉这个键值对。

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        records = dict()
        for i in magazine:
            records[i] = records.get(i, 0) + 1
        for i in ransomNote:
            if i not in records:
                return False
            records[i] = records.get(i, 0) - 1
            if records[i] == 0:
                records.pop(i)
        return True
```



### 1054 - 三数之和<a id="p1054"></a>

#### 问题

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请

你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

 

 

**示例 1：**

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```

**示例 2：**

```
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
```

**示例 3：**

```
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
```



#### 解法

双指针

代码随想录：

![15.三数之和](./assets/15.三数之和.gif)

拿这个nums数组来举例，首先将数组排序，然后有一层for循环，i从下标0的地方开始，同时定一个下标left 定义在i+1的位置上，定义下标right 在数组结尾的位置上。

依然还是在数组中找到 abc 使得a + b +c =0，我们这里相当于 a = nums[i]，b = nums[left]，c = nums[right]。

接下来如何移动left 和right呢， 如果nums[i] + nums[left] + nums[right] > 0 就说明 此时三数之和大了，因为数组是排序后了，所以right下标就应该向左移动，这样才能让三数之和小一些。

如果 nums[i] + nums[left] + nums[right] < 0 说明 此时 三数之和小了，left 就向右移动，才能让三数之和大一些，直到left与right相遇为止。

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums)
        res=[]
        if not nums:
            return []
        nums.sort()
        res=[]
        for i in range(n):
            if(nums[i]>0):
                return res
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res
```



### 1055 - 四数之和<a id="p1054"></a>

#### 问题

给你一个由 `n` 个整数组成的数组 `nums` ，和一个目标值 `target` 。请你找出并返回满足下述全部条件且**不重复**的四元组 `[nums[a], nums[b], nums[c], nums[d]]` （若两个四元组元素一一对应，则认为两个四元组重复）：

- `0 <= a, b, c, d < n`
- `a`、`b`、`c` 和 `d` **互不相同**
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

你可以按 **任意顺序** 返回答案 。

 

**示例 1：**

```
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**示例 2：**

```
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
```



#### 解法

双指针去重

与[1054 - 三数之和](#p1054)类似，叠了两层for循环；而且值得关注的是优化部分的代码:

```python
if x + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:  # 优化一
    break
if x + nums[-3] + nums[-2] + nums[-1] < target:  # 优化二
    continue
```

这一部分的含义是：由于数组是被排序过的，所以当初始的最小元素和大于target，说明整体不需要再循环了，因为后续的值只会更大；而如果当前最大的值仍然比target小，就将指针向右移动。(这一部分三层和两层是一样的)

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 难点在于去重
        lenth = len(nums)
        nums.sort()
        ans = []
        for i in range(lenth - 3):
            x = nums[i]
            # 去重
            if i and nums[i] == nums[i - 1]:
                continue
            if x + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:  # 优化一
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:  # 优化二
                continue
            for j in range(i + 1, lenth - 2):
                y = nums[j]
                if j > i + 1 and y == nums[j - 1]:  # 跳过重复数字
                    continue
                if x + y + nums[j + 1] + nums[j + 2] > target:  # 优化一
                    break
                if x + y + nums[-2] + nums[-1] < target:  # 优化二
                    continue
                c = j + 1
                d = lenth - 1
                while c < d:
                    s = x + y + nums[c] + nums[d]
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:
                        ans.append([x, y, nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]:
                            d -= 1
        return ans
```

字典法

求出target和三个元素的差值，判断这个差值是否重复，

如何判断重复？只要目标值val和前面的三元素之一重复，就说明val可能重复了，但是`if freq[val] > count`可以判断是否真正的重复：如果它出现的频率大于可能重复的次数，就说明它一定不重复且存在。

如果不重复就将其加入最终结果。

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 创建一个字典来存储输入列表中每个数字的频率
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # 创建一个集合来存储最终答案，并遍历4个数字的所有唯一组合
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in freq:
                        # 确保没有重复
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if freq[val] > count:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
        
        return [list(x) for x in ans]
```



### 1056 - 反转字符串中的单词<a id="p1056"></a>

#### 问题

给你一个字符串 `s` ，请你反转字符串中 **单词** 的顺序。

**单词** 是由非空格字符组成的字符串。`s` 中使用至少一个空格将字符串中的 **单词** 分隔开。

返回 **单词** 顺序颠倒且 **单词** 之间用单个空格连接的结果字符串。

**注意：**输入字符串 `s`中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

 

**示例 1：**

```
输入：s = "the sky is blue"
输出："blue is sky the"
```

**示例 2：**

```
输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。
```

**示例 3：**

```
输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
```



#### 解法

调库

```python
return " ".join(s.split()[::-1])
```

双指针，切割后双向奔赴

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # 切割，双向奔赴反转
        lst = s.split()
        l, r = 0, len(lst) - 1
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        return " ".join(lst)
```



### 1057 - 重复的子字符串<a id="p1057"></a>

#### 问题

给定一个非空的字符串 `s` ，检查是否可以通过由它的一个子串重复多次构成。

 

**示例 1:**

```
输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。
```

**示例 2:**

```
输入: s = "aba"
输出: false
```

**示例 3:**

```
输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
```



#### 解法

代码随想录：移动匹配

当一个字符串s：abcabc，内部由重复的子串组成，那么这个字符串的结构一定是这样的：

![图一](./assets/20220728104518.png)

也就是由前后相同的子串组成。

那么既然前面有相同的子串，后面有相同的子串，用 s + s，这样组成的字符串中，后面的子串做前串，前面的子串做后串，就一定还能组成一个s，如图：

![图二](./assets/20220728104931.png)

所以判断字符串s是否由重复子串组成，只要两个s拼接在一起，里面还出现一个s的话，就说明是由重复子串组成。

当然，我们在判断 s + s 拼接的字符串里是否出现一个s的的时候，**要刨除 s + s 的首字符和尾字符**，这样避免在s+s中搜索出原来的s，我们要搜索的是中间拼接出来的s。



下面是使用in方法

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        ss = s[1:] + s[:-1]             
        return s in ss
```

下面是使用find方法

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        ss = s[1:] + s[:-1] 
        print(ss.find(s))              
        return ss.find(s) != -1
```



### 1058 - 删除字符串中的所有相邻重复项<a id="p1058"></a>

#### 问题

给出由小写字母组成的字符串 `S`，**重复项删除操作**会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

 

**示例：**

```
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
```



#### 解法

使用栈

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        for i in s:
            if result and i == result[-1]:
                result.pop()
            else:
                result.append(i)
        return "".join(result)
```

使用双指针

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]
            
            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])
```



### 1059 - 逆波兰表达式求值<a id="p1059"></a>

#### 问题

给你一个字符串数组 `tokens` ，表示一个根据 [逆波兰表示法](https://baike.baidu.com/item/逆波兰式/128437) 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

**注意：**

- 有效的算符为 `'+'`、`'-'`、`'*'` 和 `'/'` 。
- 每个操作数（运算对象）都可以是一个整数或者另一个表达式。
- 两个整数之间的除法总是 **向零截断** 。
- 表达式中不含除零运算。
- 输入是一个根据逆波兰表示法表示的算术表达式。
- 答案及所有中间计算结果可以用 **32 位** 整数表示。

 

**示例 1：**

```
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
```

**示例 2：**

```
输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
```

**示例 3：**

```
输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```



#### 解法

**逆波兰表达式：**

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。

- 平常使用的算式则是一种中缀表达式，如 `( 1 + 2 ) * ( 3 + 4 )` 。
- 该算式的逆波兰表达式写法为 `( ( 1 2 + ) ( 3 4 + ) * )` 。

逆波兰表达式主要有以下两个优点：

- 去掉括号后表达式无歧义，上式即便写成 `1 2 + 3 4 + * `也可以依据次序计算出正确结果。
- **适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中**

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 栈：遇到数字则入栈，遇到运算符则去除栈顶的两个数字进行计算，并将结果压入栈中
        lst = []
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                lst.append(int(i))
            elif i == "+":
                a = lst.pop()
                b = lst.pop()
                lst.append(a + b)
            elif i == "-":
                a = lst.pop()
                b = lst.pop()
                lst.append(b - a)
            elif i == "*":
                a = lst.pop()
                b = lst.pop()
                lst.append(a * b)
            elif i == "/":
                a = lst.pop()
                b = lst.pop()
                lst.append(int(b / a))

        return lst[0]
```

使用字典后的简化版本

```python
from operator import add, sub, mul

class Solution:
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))  # 第一个出来的在运算符后面
        return stack.pop()
```



### 1060 - 滑动窗口的最大值<a id="p1060"></a>

#### 问题

给你一个整数数组 `nums`，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 *滑动窗口中的最大值* 。

 

**示例 1：**

```
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**示例 2：**

```
输入：nums = [1], k = 1
输出：[1]
```



#### 解法

代码随想录

> 来看一下单调队列如何维护队列里的元素。
>
> 动画如下：
>
> ![239.滑动窗口最大值](./assets/239.滑动窗口最大值.gif)

> 对于窗口里的元素{2, 3, 5, 1 ,4}，单调队列里只维护{5, 4} 就够了，保持单调队列里单调递减，此时队列出口元素就是窗口里最大元素。
>
> 此时大家应该怀疑单调队列里维护着{5, 4} 怎么配合窗口进行滑动呢？
>
> 设计单调队列的时候，pop，和push操作要保持如下规则：
>
> 1. pop(value)：如果窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素，否则不用任何操作
> 2. push(value)：如果push的元素value大于入口元素的数值，那么就将队列入口的元素弹出，直到push元素的数值小于等于队列入口元素的数值为止
>
> 保持如上规则，每次窗口移动的时候，只要问que.front()就可以返回当前窗口的最大值。
>
> 为了更直观的感受到单调队列的工作过程，以题目示例为例，输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3，动画如下：

> ![239.滑动窗口最大值-2](./assets/239.滑动窗口最大值-2.gif)



目前最优解法，使用collection包下面的deque数据结构进行操作，具体实现是单调队列。

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]
        n=len(nums)
        deque=collections.deque()
        for i in range(k):
            while deque and nums[i]>deque[-1]:
                deque.pop()
            deque.append(nums[i])
        l.append(deque[0])
        for i in range(k,n):
            if deque[0]==nums[i-k]:
                deque.popleft()
            while deque and nums[i]>deque[-1]:
                deque.pop()
            deque.append(nums[i])
            l.append(deque[0])
        return l
```

正常人的暴力解法，LeetCode通过90%

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        # 记录最大值的索引，最大索引以后方为主
        # 一旦索引越界就更新最大值并记录索引
        max_num = max(nums[0:k])
        max_index = 0
        for i in range(k):
            if nums[i] == max_num:
                max_index = i
        result = [max_num]

        for i in range(k, len(nums)):
            if i - k  + 1> max_index:
                max_num = max(nums[i - k + 1:i + 1])
                for j in range(i - k + 1, i + 1):
                    if nums[j] == max_num:
                        max_index = j
            elif nums[i] > max_num:
                max_num = nums[i]
            result.append(max_num)
        return result
```



### 1061 - 前k个高频元素<a id="p1061"></a>

#### 问题

给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

 

**示例 1:**

```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```

**示例 2:**

```
输入: nums = [1], k = 1
输出: [1]
```



#### 解法

使用哈希表进行暴力解法，其中用到了字典的`zip()`方法：将字典的键和值反转。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        暴力
        result = []
        dirt = {}
        for i in nums:
            dirt[i] = dirt.get(i, 0) + 1
        for i in range(k):
            max_index = max(zip(dirt.values(), dirt.keys()))
            result.append(max_index[1])
            dirt.pop(result[-1])
        return result
```

使用列表代替小顶堆，也是暴力解法，不过速度要快很多。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        lst = []
        dirt = {}
        for i in nums:
            dirt[i] = dirt.get(i, 0) + 1

        for key, value in dirt.items():
            lst.append((value, key))
        lst.sort()
        for i in range(len(lst) - 1, len(lst) - k - 1, -1):
            result.append(lst[i][-1])
        return result
```

使用headq模块，是对堆的相关操作的模块。

关于headq模块的使用可以参考[Python中heapq模块浅析_heapq.heappush-CSDN博客](https://blog.csdn.net/chandelierds/article/details/91357784)

代码随想录：

> ![347.前K个高频元素](./assets/347.前K个高频元素.jpg)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #时间复杂度：O(nlogk)
        #空间复杂度：O(n)
        import heapq
        #要统计元素出现频率
        map_ = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = [] #小顶堆
        
        #用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            print(pri_que)
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
                print("弹出后", pri_que)
        

        print("最终的", pri_que)
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
```













### 3001 - 替换数字<a id="p3001"></a>

#### 问题

###### 题目描述

给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。 例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。

###### 输入描述

输入一个字符串 s,s 仅包含小写字母和数字字符。

###### 输出描述

打印一个新的字符串，其中每个数字字符都被替换为了number

###### 输入示例

```
a1b2c3
```

###### 输出示例

```
anumberbnumbercnumber
```



#### 方法

字符串切割成，如果是数字就替换成number

```python
s = input()
result = ""
lst = []
for i in s:
    if ord(i) >= 48 and ord(i) <= 57:
        lst.append("number")
        continue
    lst.append(i)
    
for i in lst:
    result = result + i
    
print(result)
```



### 3002 -  右旋字符串<a id="p3002"></a>

#### 问题

###### 题目描述

字符串的右旋转操作是把字符串尾部的若干个字符转移到字符串的前面。给定一个字符串 s 和一个正整数 k，请编写一个函数，将字符串中的后面 k 个字符移到字符串的前面，实现字符串的右旋转操作。 

例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。

###### 输入描述

输入共包含两行，第一行为一个正整数 k，代表右旋转的位数。第二行为字符串 s，代表需要旋转的字符串。

###### 输出描述

输出共一行，为进行了右旋转操作后的字符串。

###### 输入示例

```
2
abcdefg
```

###### 输出示例

```
fgabcde
```



#### 解法

```python
# 所谓右旋字符串，就是按照先后顺序将一定位数的字符串反转到字符串左侧
k = int(input())
s = input()
lenth = len(s)
for i in range(-1,-(k + 1),-1):
    print(s[i])
    s = s[i] + s
print(s[:lenth])
```

