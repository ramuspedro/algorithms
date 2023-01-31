# https://leetcode.com/problems/valid-parentheses/description/

# ()
# -> (, {, [ - como append
# -> ), }, ] - como pop
# se o valor não corresponder a ), }, ] = retornar falso

class Solution:
    def isValid(self, s: str) -> bool:
        corresponding = {
            ")":"(",
            "}": "{",
            "]": "["
        }

        stack = []

        for el in s:
            if el in corresponding:
                if len(stack) == 0:
                    return False
                aval = stack.pop()
                if aval != corresponding[el]:
                    return False
            else:
                stack.append(el)

        if len(stack) > 0:
            return False

        return True

solution = Solution()

print("teste 1: True = ", solution.isValid("()"))
print("teste 2: True = ", solution.isValid("()[]{}"))
print("teste 3: False = ", solution.isValid("(]"))
print("teste 4: False = ", solution.isValid("((()"))
print("teste 5: False = ", solution.isValid("[]]]"))