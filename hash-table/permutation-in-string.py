class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        left = 0
        current_str = ""
        for right in range(len(s2)):
            while(right - left + 1 > window_size):
                left += 1
            if(right - left + 1 == window_size and sorted(s1) == sorted(s2[left:right+1])):
                return True
        return False


        