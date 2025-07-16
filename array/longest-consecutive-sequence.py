#clarifying question: what if the array is empty? what should I return?
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(set(nums))
        if not nums_sorted:
            return 0
        prev = nums_sorted[0]
        hashmap = {}
        consective_term = 1
        hashmap[consective_term] = [prev]
        for num in nums_sorted[1::]:
            if abs(num - prev) > 1:
                consective_term += 1
                prev = num
                continue
            elif abs(num - prev) == 1:
                hashmap[consective_term].append(num)
                prev = num
        return max(len(v) for v in hashmap.values())

                
