class Solution:
    def infix_to_postfix(self, infix):
        postfix = []
        stack = []

        operators = ["/", "*", "+", "-", "("]
        operators_set = set(operators)
        priority = {k: i for i, k in enumerate(operators)}


        for token in infix:
            if token == "(":
                stack.append(token)
            elif token == ")":
                while stack[-1] != "(":
                    postfix.append(stack.pop())
            elif token not in operators_set:
                postfix.append(token)
            else: 
                while stack and priority[stack[-1]] >= priority[token]:
                    postfix.append(stack.pop())
                stack.append(token)
        
        while stack:
            postfix.append(stack.pop())
        
        return postfix


    def calculate(self, s):
        stack = []
        # op_not_sum = []
        # s_list = [el for el in s if el != " "]
        s_list = []
        ops = set(["+", "-", "*", "/"])
        for el in s:
            if el == " ":
                continue
            elif s_list and el not in ops and s_list[-1] not in ops:
                s_list[-1] += el
            else:
                s_list.append(el)
        priority = []
        for i in range(len(s_list)):
            if s_list[i] == "-":
                s_list[i+1] = "-"+s_list[i+1]
            elif s_list[i] == "+":
                continue
            elif s_list[i] == "*" or s_list[i] == "/":
                priority.append(s_list[i])
            else:
                if priority:
                    op = priority.pop()
                    el2 = int(s_list[i])
                    el1 = stack.pop()
                    if op == "*":
                        stack.append(el1 * el2)
                    else:
                        stack.append(int(el1 / el2))
                else:
                    stack.append(int(s_list[i]))

        return sum(stack)

s = Solution()
# print("2 = ", s.calculate("1+1"))
# print("4 = ", s.calculate("1+1+2"))
# print("-1 = ", s.calculate("1- 2 "))
# print("0 = ", s.calculate(" 1+1-2"))
print("7 = ", s.calculate(" 3+2*2"))
print("1 = ", s.calculate(" 3/2 "))
print("5 = ", s.calculate(" 3+5 / 2 "))
print("42 = ", s.calculate("42"))
print("43 = ", s.calculate("42+1"))
# print("6 = ", s.calculate("(1+2)+3"))
# print("12 = ", s.calculate("(1+2+4)+5"))
# print("29 = ", s.calculate("(1+2+4*5)+6"))
# print("2 = ", s.calculate("1 + 1"))
# print("3 = ", s.calculate(" 2-1 + 2 "))
# print("23 = ", s.calculate("(1+(4+5+2)-3)+(6+8)"))