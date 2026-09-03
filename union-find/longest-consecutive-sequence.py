class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        if not nums:
            return 0
        result = 1
        longest = 1
        for i in range(1, len(sort_nums)):
            if sort_nums[i-1] + 1 == sort_nums[i]:
                result += 1
                longest = max(longest, result)
            elif sort_nums[i-1] == sort_nums[i]:
                continue
            else:
                result = 1
        return longest
                


            
        