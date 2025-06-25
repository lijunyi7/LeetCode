class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table and hash_table[complement] != i:
                return [i, hash_table[complement]]
            


        