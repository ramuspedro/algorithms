# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = []
    #     expect_sum = []
    #     max_count = 0

    #     for ch in s:
    #         if ch == "(":
    #             stack.append("(")
    #             expect_sum.append(2)
    #         else:
    #             if stack and stack[-1] == "(":
    #                 stack.pop()
    #                 expect_sum[-1] = sum(expect_sum)
    #                 if expect_sum[-1] > max_count:
    #                     max_count = expect_sum[-1]
    #             else:
    #                 expect_sum = []

    #     return max_count
    def longestValidParentheses(self, s: str) -> int:
        total = []
        stack = []

        for ch in s:
            if ch == "(":
                stack.append("(")
                total.append(0)
            elif ch == ")" and stack and stack[-1] == "(":
                stack.pop()
                total.append(2)
                count = 0
                # [2,0,2,0,2]
                while len(total) > 1 and (count < 1 or total[-2] != 0):
                    val = total.pop()
                    if total[-1] == 0:
                        count += 1
                    total[-1] += val
            else:
                total.append(0)

        return max(total) if total else 0

s = Solution()

print("2 = ", s.longestValidParentheses("(()"))
print("4 = ", s.longestValidParentheses(")()())"))
# # # ( -> 1 3 5  
# # # ) -> 0 2 4 6
print("0 = ", s.longestValidParentheses(""))
print("2 = ", s.longestValidParentheses("()(()"))
# # ( -> 0 2 3  
# # ) -> 1 4

print("6 = ", s.longestValidParentheses("()(())"))
print("4 = ", s.longestValidParentheses(")()())()()("))

print("4 = ", s.longestValidParentheses("()((())"))