class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap_s = {}
        hashmap_t = {}
        for i in s:
            hashmap_s[i] = hashmap_s.get(i, 0) + 1
        for j in t:
            hashmap_t[j] = hashmap_t.get(j, 0) + 1
        return hashmap_s == hashmap_t

        