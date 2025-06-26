class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs or len(strs) == 1:
            return [strs]
        
        hashmap = {}
        for word in strs:
            sorted_word = "".join(sorted(word)) 
            if sorted_word not in hashmap:       
                hashmap[sorted_word] = []
            hashmap[sorted_word].append(word)
        
        result = []
        for value in hashmap.values():
            result.append(value)
        return result



        