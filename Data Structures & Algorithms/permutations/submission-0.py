class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(permutation, used):
            if len(permutation) == len(nums):
                permutations.append(permutation.copy())
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                
                permutation.append(nums[i])
                used.add(i)
                backtrack(permutation, used)
                permutation.pop()
                used.remove(i)
            
        backtrack([], set())
        return permutations