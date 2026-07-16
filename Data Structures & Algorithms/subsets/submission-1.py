class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(subset, index):
            subsets.append(subset.copy())

            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
        
        backtrack([], 0)
        return subsets
