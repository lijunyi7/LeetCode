class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        i = 0
        result = []

        def twoSum(target: int, l: list[int]):
            left = 0
            right = len(l) - 1
            while(right > left):
                if l[right] + l[left] == target:
                    if ([l[right], l[left], -target] not in result):
                        result.append([l[right], l[left], -target])
                    left += 1
                    right -= 1
                elif l[right] + l[left] > target:
                    right -= 1
                else:
                    left += 1
        
        while i < len(nums) and nums[i] <= 0:
                current = nums[i]
                target = -current
                twoSum(target, nums[i+1:])
                i+=1
        return result

