class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        start_vals = []
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            start_vals.append(num)
        
        lengths = []
        for val in start_vals:
            curr = val
            length = 1
            while curr + 1 in nums_set:
                curr = curr + 1
                length += 1
            lengths.append(length)
        
        return max(lengths)
            
            


