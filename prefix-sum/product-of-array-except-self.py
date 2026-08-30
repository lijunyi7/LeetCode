class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre = [1] * length
        post = [1] * length
        for i in range(length):
            if i == 0:
                pre[i] = 1
                continue
            pre[i] = pre[i -1] * nums[i - 1]
        for i in range(length - 1, -1, -1):
            if (i - length) == -1:
                post[i - length] = 1
                continue
            post[i - length] = post[i - length + 1] * nums[i - length + 1]
        
        return [post[i] * pre[i] for i in range(length)]

        