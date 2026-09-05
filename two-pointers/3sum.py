class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        i = 0
        result = []

        def twoSum(target: int, start: int):
            left = start
            right = len(nums) - 1

            while right > left:
                total = nums[right] + nums[left]

                if total == target:
                    result.append([nums[right], nums[left], -target])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total > target:
                    right -= 1
                else:
                    left += 1

        while i < len(nums) and nums[i] <= 0:

            # Skip duplicate current values
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            current = nums[i]
            target = -current
            twoSum(target, i + 1)
            i += 1

        return result