# 题目以及解析

LeetCode：100x



### 1001：两数之和

Tag：数组、哈希表

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



### 1002：回文数

Tag：数学

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



### 1003：罗马数字转整数

Tag：字符串、哈希表、数学

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



### 1004：最长公共前缀

Tag：字符串

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



### 1005：有效的括号

Tag：栈、字符串

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



### 1006：合并两个有序链表

Tag：递归、链表

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



### 1007 ：删除有序数组中的重复项

Tag：数组、双指针

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



### 1008：移除元素

Tag：数组、双指针

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
```



### 1009：找出字符串中第一个匹配项的下标

Tag：双指针、字符串

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



### 1010：搜索插入位置

Tag：数组、二分查找

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

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if target <= i:
                return nums.index(i)
        return len(nums)
```



### 1011：最后一个单词的长度

Tag：字符串

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



### 1012：加一

Tag：数组、数学

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



### 1013：二进制求和

Tag：位运算、数学、字符串

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



### 1014：x的平方根

Tag：数学、二分查找

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



### 1015：爬楼梯

Tag：记忆化搜索、数学、动态规划

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



### 1016：删除排序链表中的重复元素

Tag：链表

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



### 1017：合并两个有序数组

Tag：数组、指针、双指针

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





### 1018：二叉树的中序遍历

Tag：栈、树、深度优先遍历

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



