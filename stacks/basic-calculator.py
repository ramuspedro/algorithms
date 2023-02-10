class Solution:
    def is_digit(self, n):
        try:
            int(n)
            return True
        except:
            return  False

    def calculate(self, s):
        i = 0
        cur = prev = 0
        res = [0]
        cur_operation = "+"
        cur_stack = [] 
        prev_stack = []
        ops_stack = []
        s = list(s)

        while i < len(s):
            cur_char = s[i]
            if self.is_digit(cur_char):
                while i < len(s) and self.is_digit(s[i]):
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1

                if cur_operation == "+":
                    res[-1] += cur
                    prev = cur
                elif cur_operation == "-":
                    res[-1] -= cur
                    prev = -cur
                elif cur_operation == "*":
                    res[-1] -= prev
                    res[-1] += prev*cur
                    prev = prev*cur
                else:
                    res[-1] -= prev
                    res[-1] += int(prev/cur)
                    prev = int(prev/cur)
                cur = 0
            elif cur_char == "(":
                ops_stack.append(cur_operation)
                cur_stack.append(cur)
                prev_stack.append(prev)
                res.append(0)
                cur = prev = 0
                cur_operation = "+"
            elif cur_char == ")":
                cur_operation = ops_stack.pop()
                prev = prev_stack.pop()
                cur = 0
                s[i] = str(res.pop())
                i -= 1
            elif cur_char != " ":
                cur_operation = cur_char
            i += 1

        return sum(res)



s = Solution()
# print("2 = ", s.calculate("1+1"))
# print("4 = ", s.calculate("1+1+2"))
# print("-1 = ", s.calculate("1- 2 "))
# print("0 = ", s.calculate(" 1+1-2"))
# print("7 = ", s.calculate(" 3+2*2"))
# print("1 = ", s.calculate(" 3/2 "))
# print("5 = ", s.calculate(" 3+5 / 2 "))
# print("42 = ", s.calculate("42"))
# print("43 = ", s.calculate("42+1"))
# print("6 = ", s.calculate("(1+2)+3"))
# print("9 = ", s.calculate("(1+2)*3"))
# print("4 = ", s.calculate("(1+(1+2))"))
# print("16 = ", s.calculate("(2*((1+3)*2)"))
# print("12 = ", s.calculate("(1+2+4)+5"))
# print("29 = ", s.calculate("(1+2+4*5)+6"))
# print("2 = ", s.calculate("1 + 1"))
# # print("3 = ", s.calculate(" 2-1 + 2 "))
# print("23 = ", s.calculate("(1+(4+5+2)-3)+(6+8)"))
# print("8 = ", s.calculate("2*((4))"))
# print("16 = ", s.calculate("2*((4)*2)"))
# print("32 = ", s.calculate("2*((4*2)*2)"))
print("3 = ", s.calculate("1-(-2)"))