"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

https://leetcode.com/problems/two-sum/

"""

class Solution:

    """
    brute force: Time: O(n^2)  Space: O(1)
    Runtime: 4652 ms, faster than 15.24% of Python3 online submissions for Two Sum.
    Memory Usage: 12.8 MB, less than 87.21% of Python3 online submissions for Two Sum.
    """
    def twoSum1(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    """
    Time: O(nlogn)  Space: O(n)
    Runtime: 36 ms, faster than 99.59% of Python3 online submissions for Two Sum.
    Memory Usage: 13.3 MB, less than 55.28% of Python3 online submissions for Two Sum.
    """
    def twoSum2(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        l = len(nums)
        index = [i for i in range(l)]
        index.sort(key=lambda x: nums[x]) # Time: O(nlogn), Space: O(logn)
        left = 0
        right = l - 1
        while left < right:
            i = index[left]
            j = index[right]
            total = nums[i] + nums[j]
            if total == target:
                return [i, j] if i < j else [j, i]
            elif total > target:
                right -= 1
            else:
                left += 1

    """
    Time: O(n)  Space: O(n)
    Runtime: 36 ms, faster than 99.59% of Python3 online submissions for Two Sum.
    Memory Usage: 15.3 MB, less than 5.08% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        l = len(nums)
        values = dict([(nums[i], i) for i in range(l)])
        for i in range(l):
            diff = target - nums[i]
            if diff in values and i != values[diff]:
                return [i, values[diff]]


import unittest

s = Solution()

class TestSolution(unittest.TestCase):

    def test1(self):
        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(s.twoSum([2, 70, 7, 15], 9), [0, 2])
        self.assertEqual(s.twoSum([2, 70, -7, 15], -5), [0, 2])
        self.assertEqual(s.twoSum([3, 2, 4], 6), [1, 2])

if __name__ == '__main__':
    unittest.main()
