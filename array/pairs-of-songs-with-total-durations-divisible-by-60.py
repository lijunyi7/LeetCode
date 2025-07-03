class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = 0
        remainder_counts = {}

        for t in time:
            r = t % 60
            complement = (60 - r) % 60

            if complement in remainder_counts:
                count += remainder_counts[complement]
                
            if r in remainder_counts:
                remainder_counts[r] += 1
            else:
                remainder_counts[r] = 1

        return count
