class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        result = []
        for interval in intervals[1::]:
            if interval[0] <= (right - left) + 1:
                if interval[0] < left:
                    left = interval[0]
                if interval[1] > right:
                    right = interval[1]
            else:
                left = interval[0]
                right = interval[1]
            result.append([left, right])
        return result
            
            


        