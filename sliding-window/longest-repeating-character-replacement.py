class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_tracker = {}
        left = 0
        right = 0
        max_freq = 0
        result = 0
        for right in range(len(s)):
            freq_tracker[s[right]] = freq_tracker.get(s[right], 0) + 1
            max_freq = max(max_freq, freq_tracker[s[right]])
            while((right - left + 1) - max_freq > k):
                freq_tracker[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


                
        