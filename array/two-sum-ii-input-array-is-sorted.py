"clarifying question: what if the input arry is empty, what shoudl I return "
"What if there is only one number"
"What if there is no number that sum to the traget"
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Initial thought: 
        using two pinters, one at the begaining of the array and one at the end
        add them together, compare the result with target, if target is smaller then the sum, move the left pointer to right and vice versa
        """
        if len(numbers) <= 1:
            return []
        right_index = 0
        left_index = -1
        while right_index != left_index + len(numbers):
            curr_sum = numbers[right_index] + numbers[left_index]
            if curr_sum == target:
                return [right_index + 1, left_index + + len(numbers) + 1]
            elif curr_sum < target:
                right_index += 1
            else:
                left_index -= 1
        return []

           


               
        

        