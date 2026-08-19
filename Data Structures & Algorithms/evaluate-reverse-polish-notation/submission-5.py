class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops_stack = []
        for i in range(len(tokens)):
            if tokens[i]   == "*":
                tmpb = ops_stack.pop()
                tmpa = ops_stack.pop()
                ops_stack.append(tmpa*tmpb)
            elif tokens[i] == "-":
                tmpb = ops_stack.pop()
                tmpa = ops_stack.pop()
                ops_stack.append(tmpa-tmpb)
            elif tokens[i] == "+":
                tmpb = ops_stack.pop()
                tmpa = ops_stack.pop()
                ops_stack.append(tmpa+tmpb)
            elif tokens[i] == "/":
                tmpb = ops_stack.pop()
                tmpa = ops_stack.pop()
                ops_stack.append(int(tmpa/tmpb))
            else:
                ops_stack.append(int(tokens[i]))
        return ops_stack[len(ops_stack)-1]
        