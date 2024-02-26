'''
    最终返回值是数组的长度+

    经典问题在于：
    对于本体做出的删除操作，如空间复杂度为O(1)
    在使用for循环(for i in nums)的条件下，对nums做出更改，实际上会产生错误：
        即(for i in nums)这一用法的底层实际上依然是(for i in range())
'''
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