class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        add = 0
        sub = 0
        mult = 1
        divid = 1

        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stk.append(int(tokens[i]))
            else:
                a = stk.pop()
                b = stk.pop()

                if tokens[i] == "+":
                    stk.append(a + b)
                elif tokens[i] == "-":
                    stk.append(b - a)
                elif tokens[i] == "*":
                    stk.append(a * b)
                else:
                    stk.append(int(float(b) / a))
        
        return stk[-1]
                

        