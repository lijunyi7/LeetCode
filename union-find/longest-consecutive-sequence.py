class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        result = 1
        for i in range(1, len(sort_nums)):
            if sort_nums[i-1] + 1 == sort_nums[i]:
                result += 1
            elif sort_nums[i-1] == sort_nums[i]:
                continue
            else:
                reuslt = 1
        return result
                


            
        