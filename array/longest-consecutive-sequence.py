#clarifying question: what if the array is empty? what should I return?
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = set(nums)
        longest_streak = 0
        for num in nums_sorted:
            if num - 1 not in nums_sorted:
                curr_num = num
                curr_streak = 1
                while curr_num + 1 in nums_sorted:
                    curr_streak += 1
                    curr_num += 1
                longest_streak = max(curr_streak, longest_streak)
        return longest_streak