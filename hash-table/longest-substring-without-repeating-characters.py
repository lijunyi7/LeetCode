class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_len = 0
        current_win_len = 0
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
            longest_len = max(longest_len, right - left)
        return longest_len
            
            

        return longest_len





            
        