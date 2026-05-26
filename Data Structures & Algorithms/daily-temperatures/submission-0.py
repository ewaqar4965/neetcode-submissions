class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i, val in enumerate(temperatures):
            while stk and val > stk[-1][0]:
                stkV, stkI = stk.pop()
                res[stkI] = i - stkI
                
            stk.append([val, i])
        
        return res