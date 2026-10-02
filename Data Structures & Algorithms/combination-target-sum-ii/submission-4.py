class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # O(nlogn)
        combinations = []

        def backtrack(index, combination, curr_sum):
            if curr_sum == target:
                combinations.append(combination.copy())
            
            for i in range(index, len(candidates)):
                if i - index and candidates[i] == candidates[i - 1]:
                    continue
                
                if curr_sum + candidates[i] > target:
                    break
                
                combination.append(candidates[i])
                backtrack(i + 1, combination, curr_sum + candidates[i])
                combination.pop()
        
        backtrack(0, [], 0)
        return combinations

# 1,2,2,3,4,5, target = 7

# 0, [], 0
#   1, [1], 1
#       2, [1, 2], 3
#           3, [1, 2, 2], 5 x
#           4, [1, 2, 3], 6 x
#           5, [1, 2, 4], 7 *
#       4, [1, 3], 4
#           5, [1, 3, 4], 8 x