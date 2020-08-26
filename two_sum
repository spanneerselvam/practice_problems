'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(1, len(nums)-1):
                if i != j:
                    sum_value = nums[i] + nums[j]
                    if sum_value == target:
                        l = list()
                        l.append(i)
                        l.append(j)
                        return l
                    
a = Solution()
print(a.twoSum([2, 7, 11, 15], target = 9))
