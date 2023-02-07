class Solution:
    def evalRPN(self, tokens):
        priority = set(["+", "-", "*", "/"])
        stack = []

        for el in tokens:
            if el not in priority:
                stack.append(el)
            else:
                el2 = eval(stack.pop())
                el1 = eval(stack.pop())
                res = 0
                if el == "+":
                    res = el1 + el2
                elif el == "-":
                    res = el1 - el2
                elif el == "*":
                    res = el1 * el2
                elif el == "/":
                    res = el1 / el2
                stack.append(str(int(res)))

        return eval(stack[0])

s = Solution()

# print("6 = ", s.evalRPN(["4","13","5","/","+"]))
print("22 = ", s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))