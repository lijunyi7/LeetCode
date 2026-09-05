class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum():
                string += i
        string_b= ""
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                string_b += s[i]
        return string.lower() == string_b.lower()
    


        