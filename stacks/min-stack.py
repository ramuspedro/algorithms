# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_temp = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack_temp) == 0:
            self.stack_temp.append(val)
        else:
            self.stack_temp.append(min(val, self.stack_temp[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.stack_temp.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack_temp[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()