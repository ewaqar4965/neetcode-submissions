class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stk.append(s[i])
            
            else:
                if not stk:
                    return False
                
                if ((s[i] == ']' and stk[-1] != '[') or (s[i] == '}' and stk[-1] != '{') or (s[i] == ')' and stk[-1] != '(')):
                    return False
                
                stk.pop()
        
        return len(stk) == 0

        