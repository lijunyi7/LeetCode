class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(time)-1):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count

        