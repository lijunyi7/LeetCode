class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            key = tuple(sorted(s))
            hashmap.setdefault(key, []).append(s)
        return list(hashmap.values())
            
        
          


