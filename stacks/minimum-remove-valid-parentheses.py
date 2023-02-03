# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    # def minRemoveToMakeValid(self, s: str) -> str:
    #     mapping = {
    #         ")": [],
    #         "(": []
    #     }

    #     for i in range(len(s)):
    #         if s[i] in mapping:
    #             mapping[s[i]].append(i)

    #     left = []
    #     for pos in mapping["("]:
    #         if pos < mapping[")"][-1]:
    #             mapping[")"] = mapping[")"][1:]
    #         else:
    #             left.append(pos)

    #     result = ""
    #     evaluate = mapping[")"] + left

    #     for i in range(len(s)):
    #         if i not in evaluate:
    #             result += s[i]
        
    #     return result
    def minRemoveToMakeValid(self, s: str) -> str:
        pos = []
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                pos.append(i)
                stack.append("(")
            elif s[i] == ")" and stack and stack[-1] == "(":
                pos.pop()
                stack.pop()
            elif s[i] == ")":
                pos.append(i)
                stack.append(")")

        result = ""
        set_pos = set(pos)
        for i in range(len(s)):
            if i not in set_pos:
                result += s[i]

        return result


s = Solution()
print("()() = ", s.minRemoveToMakeValid("())()((("))
print("a)b(c)d = ", s.minRemoveToMakeValid("ab(c)d"))
# print("())(( = ", s.minRemoveToMakeValid(""))
# {
#     ")": [1,2]
#     "(": [0,3,4]
# }

