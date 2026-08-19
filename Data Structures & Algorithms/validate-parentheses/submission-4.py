class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hs = {"}":"{","]":"[",")":"("}
        for c in s:
            if c in "}])" and len(stk)>0:
                if stk[len(stk)-1] != hs[c]:
                    return False
                else:
                    stk.pop()
            else:
                stk.append(c)
        if len(stk):
            return False
        return True