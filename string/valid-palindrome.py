class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_filter = ''.join(c.lower() for c in s if c.isalnum())
        if not s_filter:
            return True
        return s_filter == s_filter[::-1]
