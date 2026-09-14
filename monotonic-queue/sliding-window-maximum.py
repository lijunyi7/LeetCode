class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        left = 0
        right = k - 1
        win_max = 0
        result = []
        while right in range(len(nums)):
            win_max = nums[left]
            for i in range(left, right+1):
                win_max = max(win_max, nums[i])
            result.append(win_max)
            right += 1
            left += 1
        return result

            
            


        