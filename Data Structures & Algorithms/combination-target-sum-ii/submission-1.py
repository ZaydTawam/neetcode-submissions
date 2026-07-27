class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        
        def backtrack(index, combination, curr_sum):
            if curr_sum == target:
                combinations.append(combination.copy())
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if curr_sum + candidates[i] > target:
                    continue
                
                combination.append(candidates[i])
                backtrack(i+1, combination, curr_sum + candidates[i])
                combination.pop()
        
        backtrack(0, [], 0)

        return combinations