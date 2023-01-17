class Solution:
    def subsets(self, nums):
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    def subsets3(self, nums):
        mem = {}
        val = nums.pop()
        result = [[]]
        
        if(len(nums) > 0):
            result = self.subsets(nums)

        N = len(result)
        for i in range(N):
            el = result[i] + [val]
            if(str(el) not in mem):
                result.append(el)
                mem[str(el)] = True
            
        return result

    def subsets1(self, nums):
        val = nums.pop()
        result = [[]]
        
        if(len(nums) > 0):
            result = self.subsets(nums)

        N = len(result)
        for i in range(N):
            el = result[i] + [val]
            if(el not in result):
                result.append(el)
            
        return result

    def subsets2(self, nums):
        result = [[]]

        while len(nums) > 0:
            value = nums.pop()
            N = len(result)
            for i in range(N):
                newEl = result[i] + [value]
                if newEl not in result:
                    result.append(newEl)

        return result

solution = Solution()
val = [1,2,3]
# print(" [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]\n", solution.subsets2(val))
print(" [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]\n", solution.subsets(val))