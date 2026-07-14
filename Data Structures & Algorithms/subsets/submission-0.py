class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def dfs(path, index):
            subsets.append(path.copy())

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()
        
        dfs([], 0)
        return subsets
