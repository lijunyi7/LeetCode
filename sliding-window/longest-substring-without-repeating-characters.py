class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        longest_len = 0
        current_win_len = 0
        left = 0
        right = 0
        for i in range(len(s)):
            if(s[i] not in sub):
                sub += s[i]
                current_win_len += 1
                right += 1
                longest_len = max(longest_len, len(sub))
            else:
                # longest_len = max(longest_len, current_win_len, right - left)
                left = right
                sub = s[left]
                current_win_len = 0
        return longest_len





            
        