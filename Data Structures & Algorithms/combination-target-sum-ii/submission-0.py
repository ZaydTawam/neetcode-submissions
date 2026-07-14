class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        print(candidates)
        def backtrack(combination, curr_sum, index):
            if curr_sum == target:
                combinations.append(combination.copy())

            for i in range(index, len(candidates)):
                if i != index and candidates[i - 1] == candidates[i]:
                    continue
                if curr_sum + candidates[i] > target:
                    continue
                combination.append(candidates[i])
                backtrack(combination, curr_sum + candidates[i], i + 1)
                combination.pop()
        
        backtrack([], 0, 0)
        return combinations