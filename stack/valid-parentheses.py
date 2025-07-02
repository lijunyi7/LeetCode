class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashmap = {'(':')', '[':']', '{': '}'}
        for p in s:
            if p in hashmap.keys():
                stack.append(p)
            elif not stack:
                return False
            else:
                open_pra = stack.pop()
                if(hashmap[open_pra] != p):
                    return False
        return not stack


        

        