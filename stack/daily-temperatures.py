class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while(stack and temperatures[i] > temperatures[stack[-1]]):
                last_temp_pos = stack.pop()
                results[last_temp_pos] = i - last_temp_pos
            stack.append(i)
        return results



           
                    
                
        