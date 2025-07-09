#The O(1) space complexity version
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        # left side
        answer[0] = 1
        # 1 because we already got the answer[0]
        for i in range(1, length):
            # prev times the one before index itself
            answer[i] = answer[i-1] * nums[i -1]
        
        R = 1
        # right side directly 1 because we can only use answer
        # and right now the answer alreadt stored the left side values
        for i in reversed (range(length)):
            answer[i] = R * answer[i]
            R *= nums[i]
        
        return answer



        