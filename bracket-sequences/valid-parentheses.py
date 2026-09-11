class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in hash_map.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                poped = stack.pop()
                if hash_map[poped] != i:
                    return False
        return not stack

        