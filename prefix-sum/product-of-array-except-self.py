class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_arr = [0] * len(nums)
        right_arr = [0] * len(nums) 
        result = [0] * len(nums)
        # for the first element in nums, the left side is 1
        # as there is no index prev to it       
        left_arr[0] = 1
        #get the left side
        for i in range(1,len(nums)):
            # becuase you don't want to include i itself
            # and the multiplication is cumulative you just have
            # to multiple the prev one to get the answer
            left_arr[i] = left_arr[i - 1] * nums[i - 1]
        #because we want to calculte from the right to left
        # so we set the last index to 1
        right_arr[len(nums)-1] = 1
        for i in reversed(range(len(nums) -1)):
            right_arr[i] = right_arr[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            result[i] = left_arr[i] * right_arr[i]
        
        return result

       