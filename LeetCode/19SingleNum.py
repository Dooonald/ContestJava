# -*- coding:UTF-8 -*-

'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Subscribe to see which companies asked this question

Show Tags
Show Similar Problems
'''



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()

        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)

        return list(s)[0]

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]
        for i in range(1, len(nums)):
            print(ans, nums[i], ans ^ nums[i])
            ans = ans ^ nums[i]
        return ans


if __name__ == '__main__':


    print(Solution().singleNumber2([1,2,1]))
