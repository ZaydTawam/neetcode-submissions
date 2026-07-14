class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        def backtrack(subset, index):
            subsets.append(subset.copy())

            for i in range(index, len(nums)):
                if i != index and nums[i - 1] == nums[i]:
                    continue
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
        
        backtrack([], 0)
        return subsets
