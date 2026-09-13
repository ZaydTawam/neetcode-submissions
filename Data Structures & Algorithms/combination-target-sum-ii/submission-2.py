class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        combinations = []

        def backtrack(index, combination, curr_sum):
            if curr_sum == target:
                combinations.append(combination.copy())
            
            for i in range(index, len(sorted_candidates)):
                if i - index and sorted_candidates[i] == sorted_candidates[i - 1]:
                    continue
                if sorted_candidates[i] + curr_sum > target:
                    continue
                
                combination.append(sorted_candidates[i])
                backtrack(i + 1, combination, sorted_candidates[i] + curr_sum)
                combination.pop()
        
        backtrack(0, [], 0)
        return combinations