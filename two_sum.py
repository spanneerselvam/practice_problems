'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    #Time complexity O(n^2)
    #Space Complexity O(n1)
    def twoSumBruteForce(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    sum_value = nums[i] + nums[j]
                    if sum_value == target:
                        return(i,j)

    def twoSum(self, nums, target):
        d = dict()
        for i in range(0, len(nums)):
            a = nums[i]
            value = target-a
            if a in d:
                for j in range(0, len(nums)):
                    if nums[j] == value:
                        return(min(i,j), max(i,j))
            else:
                d[value] = a
                
a = Solution()
l = [2, 4, 6]
target = 10
print(a.twoSumBruteForce(l, target))
print(a.twoSum(l, target))
