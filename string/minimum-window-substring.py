from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)
        if s_len < t_len:
            return ""
        if s == t:
            return s
        left = 0

        t_dic = Counter(t)
        sub_dic = {}

        matched = 0
        required = len(t_dic)

        sub_str = ""
        min_len = float("inf")
        for right in range(s_len):
            if(s[right] in t_dic):
                sub_dic[s[right]] = sub_dic.get(s[right], 0) + 1
                if (sub_dic[s[right]] == t_dic[s[right]]):
                    matched += 1
            while (matched == required):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    sub_str = s[left:right + 1]

                if(s[left] in t_dic):
                    sub_dic[s[left]] -= 1
                    if sub_dic[s[left]] < t_dic[s[left]]:
                        matched -= 1
                left += 1
        return sub_str