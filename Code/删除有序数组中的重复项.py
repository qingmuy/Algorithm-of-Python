'''
    去重
    利用Set集合进行去重
    转换为List后再排序
'''
class Solution:
    def removeDuplicates(self, nums) -> int:
        # j = 0
        # for i in nums:
        #     index = nums[j]
        #     if i == index:
        #         nums.remove(i)
        #         j += 1
        #     else:
        #         j += 1


        # i = 0
        # while(i + 1 < len(nums)):
        #     if nums[i] == nums[i + 1]:
        #         nums.remove(nums[i])
        #     else:
        #         i += 1
        # return len(set(nums))


        if len(nums)  == 0: 
            return 0
        k =  1
        for  i in range(1, len(nums)):
             if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
test = Solution()
test.removeDuplicates(nums)
print(nums)