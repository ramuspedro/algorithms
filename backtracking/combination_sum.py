class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0,[],0)

        return res

    def combinationSum1(self, candidates, target):
        result = []

        while len(candidates) > 0:
            aval = candidates[0]
            candidates = candidates[1:]
            for i in range(len(result)):
                el = result[i][1] - aval
                if el >= 0:
                    result[i][0].append(aval)
                    result[i][1] = el
                    
            compound = []
            newSum = aval
            
            while target - newSum >= 0:
                compound.append(aval)
                result.append([compound.copy(), target-newSum])
                newSum += aval
        final_result = []
        for el in result:
            if el[1] == 0:
                final_result.append(el[0])

        return final_result

solution = Solution()
# val = [2,3,6,7]
# print(" [[2, 2, 3], [7]]\n", solution.combinationSum(val,7))

val2 = [2,3,5]
print(" [[2, 2, 2, 2], [2, 3, 3], [3, 5]]\n", solution.combinationSum(val2,8))

# val3 = [2]
# print(" []\n", solution.combinationSum(val3,1))