class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for i, num in enumerate(nums):
            elements[num] = i
        
        for i, num in enumerate(nums):
            if target-num in elements:
                if i != elements[target-num]:
                    return [i, elements[target-num]]